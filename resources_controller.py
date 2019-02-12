import connexion
import six
from kubernetes.client.rest import ApiException

from swagger_server.models.resources import Resources  # noqa: E501
from swagger_server import util

from .kubernetes_client import GenericK8Client

def current_usage(infraId, nodeId):  # noqa: E501
    """Outputs the current resource usage for the whole cluster

     # noqa: E501


    :rtype: Resources
    """
    k8client = GenericK8Client(host='http://104.36.16.199:9999')
    try:
        result = k8client.custom_client('/apis/metrics.k8s.io/v1beta1/nodes/' + nodeId)
    except Exception as e:
        if e.status == 404:
            return 'Node {} not found'.format(nodeId), 404
        else:
            return 'Cannot connect to Kubernetes metrics API: {}'.format(e), 500

    return {'cpu': result['usage']['cpu'], 'mem': result['usage']['memory'], 'storage': 0}



def resources(infraId, nodeId):  # noqa: E501
    """Outputs the resources defined for the whole cluster

     # noqa: E501


    :rtype: Resources
    """
    k8client = GenericK8Client(host='http://104.36.16.199:9999')
    v1 = k8client.v1client()
    try:
        result = v1.list_node()
    except Exception as e:
        return 'Cannot connect to Kubernetes API: {}'.format(e), 500

    for node in result.items:
        if node.metadata.name == nodeId:
            return {'cpu': node.status.capacity['cpu'], 'mem': node.status.capacity['memory'], 'storage': 0}, 200

    return 'Node {} not found'.format(nodeId), 404
