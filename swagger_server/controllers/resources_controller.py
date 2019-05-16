import connexion
import six
from kubernetes.client.rest import ApiException

from swagger_server.models.resources import Resources  # noqa: E501
from swagger_server import util

from .kubernetes_client import GenericK8Client, HeketiClient
from .conf import config


def current_usage(infraId, nodeId):  # noqa: E501
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
        result = k8client.custom_client('/apis/metrics.k8s.io/v1beta1/nodes/' + nodeId)
    except Exception as e:
        if e.status == 404:
            return 'Node {} not found'.format(nodeId), 404
        else:
            return 'Cannot connect to Kubernetes metrics API: {}'.format(e), 500

    try:
        res = v1.list_node()
    except Exception as e:
        return 'Cannot connect to Kubernetes API: {}'.format(e), 500

    for node in res.items:
        if node.metadata.name == nodeId:
            cpu = util.normalize_metrics(cores=int(node.status.capacity['cpu']), cpu=result['usage']['cpu'])['cpu']

    mem = util.normalize_metrics(mem=node.status.capacity['memory'])['mem'] - util.normalize_metrics(
        mem=result['usage']['memory'])['mem']
    stor = heketi_client.get_storage_metrics()
    storage = util.normalize_metrics(storage=stor['total_bytes_free'])['storage']

    return {'cpu': cpu, 'mem': mem, 'storage': storage}


def resources(infraId, nodeId):  # noqa: E501
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

    for node in result.items:
        if node.metadata.name == nodeId:
            mem = util.normalize_metrics(mem=node.status.capacity['memory'])['mem']
            stor = heketi_client.get_storage_metrics(substring='size')
            storage = util.normalize_metrics(storage=stor['total_bytes_size'])['storage']
            return {'cpu': node.status.capacity['cpu'], 'mem': mem, 'storage': storage}, 200

    return 'Node {} not found'.format(nodeId), 404
