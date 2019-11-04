from swagger_server.models.resources import Resources  # noqa: E501
from swagger_server import util

from clients.kubernetes_client import GenericK8Client, HeketiClient
from conf.conf import config


def current_usage(infraId, nodeId=None):  # noqa: E501
    """Outputs the current resource usage for the whole cluster

     # noqa: E501


    :rtype: Resources
    """
    if infraId not in config['infra_names']:
        return 'Infrastructure Id not found in Blueprint', 404
    k8client = GenericK8Client(infra_name=infraId)
    heketi_client = HeketiClient(infra_name=infraId)
    v1 = k8client.v1client()
    try:
        if nodeId:
            result = k8client.custom_client('/apis/metrics.k8s.io/v1beta1/nodes/' + nodeId)
        else:
            result = k8client.custom_client('/apis/metrics.k8s.io/v1beta1/nodes/')
    except Exception as e:
        if nodeId and e.status == 404:
            return 'Node {} not found'.format(nodeId), 404
        else:
            return 'Cannot connect to Kubernetes metrics API: {}'.format(e), 500

    try:
        res = v1.list_node()
    except Exception as e:
        return 'Cannot connect to Kubernetes API: {}'.format(e), 500
    total_mem_usage = 0
    total_cpu_usage = 0
    total_cpu_cap = 0
    for node in res.items:
        if nodeId:
            if node.metadata.name == nodeId:
                cpu = util.normalize_metrics(cores=int(node.status.capacity['cpu']), cpu=result['usage']['cpu'])['cpu']
        elif node.metadata.name in config['infra'][infraId].keys():
            for n in result['items']:
                if n['metadata']['name'] == node.metadata.name:
                    cpu = util.normalize_metrics(cores=int(node.status.capacity['cpu']), cpu=n['usage']['cpu'])['cpu']
                    total_cpu_usage += (config['infra'][infraId][node.metadata.name]['cpu'] * (cpu / 100))
                    total_cpu_cap += config['infra'][infraId][node.metadata.name]['cpu']
                    total_mem_usage += util.normalize_metrics(mem=n['usage']['memory'])['mem']

    if total_cpu_usage and total_cpu_cap:
        total_cpu_average = total_cpu_usage / total_cpu_cap

    if nodeId:
        mem = util.normalize_metrics(mem=result['usage']['memory'])['mem']
    stor = heketi_client.get_storage_metrics()
    storage = util.normalize_metrics(storage=stor['total_bytes_free'])['storage']
    if nodeId:
        return {'cpu': cpu, 'mem': mem, 'storage': storage}
    else:
        return {'cpu': total_cpu_average, 'mem': total_mem_usage, 'storage': storage}


def resources(infraId, nodeId=None):  # noqa: E501
    """Outputs the resources defined for the whole cluster

     # noqa: E501


    :rtype: Resources
    """
    if infraId not in config['infra_names']:
        return 'Infrastructure Id not found in Blueprint', 404
    k8client = GenericK8Client(infra_name=infraId)
    heketi_client = HeketiClient(infra_name=infraId)
    v1 = k8client.v1client()
    try:
        result = v1.list_node()
    except Exception as e:
        return 'Cannot connect to Kubernetes API: {}'.format(e), 500
    cpu = 0
    mem = 0
    stor = heketi_client.get_storage_metrics(substring='size')
    storage = util.normalize_metrics(storage=stor['total_bytes_size'])['storage']
    for node in result.items:
        if nodeId:
            if node.metadata.name == nodeId:
                mem = util.normalize_metrics(mem=node.status.capacity['memory'])['mem']
                cpu = config['infra'][infraId][node.metadata.name]['cpu']
        elif node.metadata.name in config['infra'][infraId].keys():
            mem += util.normalize_metrics(mem=node.status.capacity['memory'])['mem']
            cpu += config['infra'][infraId][node.metadata.name]['cpu']

    return {'cpu': cpu, 'mem': mem, 'storage': storage}, 200
