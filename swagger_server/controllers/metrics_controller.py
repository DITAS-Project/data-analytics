import connexion
import six

from swagger_server.models.metric_res import MetricRes  # noqa: E501
from swagger_server import util


def getmetrics(infraId, nodeId, operationID, name, startTime, endTime):  # noqa: E501
    """getmetrics

    Get metric value based on meter operation id, name, timestamp # noqa: E501

    :param infraId: The infrastructure name based on the blueprint
    :type infraId: str
    :param nodeId: The node name based on the blueprint
    :type nodeId: str
    :param operationID: Operation id based on deployment blueprint
    :type operationID: str
    :param name: Name of meter
    :type name: str
    :param startTime: Start timestamp of meter
    :type startTime: str
    :param endTime: End timestamp of meter
    :type endTime: str

    :rtype: MetricRes
    """
    startTime = util.deserialize_datetime(startTime)
    endTime = util.deserialize_datetime(endTime)
    return 'do some magic!'
