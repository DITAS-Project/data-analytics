from swagger_server.models.metric_res import MetricRes  # noqa: E501
from swagger_server import util

from clients.elastic_client import ElasticClient


BASE_QUERY = {
  "_source": ["request.name", "request.operationID", "request.value", "request.unit", "request.timestamp", "request.appendix"],
  "query": {
    "bool": {
      "must": [{
        "exists": {"field": "request"}
        },
        {
          "match": {
            "request.name": ""
          }
        },
        {
          "match": {
            "request.operationID": ""
          }
        },
        {
          "range": {
            "request.timestamp": {
              "gte": "",
              "lt": ""
            }
          }
        }
      ]
    }
  }
}


def getmetrics(vdcId, operationID, name, startTime, endTime, blueprintId=None):  # noqa: E501

    """getmetrics

    Get metric value based on request operation id, name, timestamp # noqa: E501

    :param vdcId: The VDC id
    :type vdcId: str
    :param operationID: Operation id based on deployment blueprint
    :type operationID: str
    :param name: Name of request
    :type name: str
    :param startTime: Start timestamp of request
    :type startTime: str
    :param endTime: End timestamp of request
    :type endTime: str
    :param blueprintId: Blueprint id
    :type blueprintId: str


    :rtype: MetricRes
    """

    startTime = util.deserialize_datetime(startTime)
    endTime = util.deserialize_datetime(endTime)
    if not blueprintId:
        index_name = '{}-*'.format(vdcId)
    else:
        index_name = '{}-{}'.format(blueprintId, vdcId)

    BASE_QUERY['query']['bool']['must'][1]['match']['request.name'] = name
    BASE_QUERY['query']['bool']['must'][2]['match']['request.operationID'] = operationID
    BASE_QUERY['query']['bool']['must'][3]['range']['request.timestamp']['gte'] = startTime
    BASE_QUERY['query']['bool']['must'][3]['range']['request.timestamp']['lt'] = endTime

    es = ElasticClient()
    try:
        result = es.search(index_name, query=BASE_QUERY)
    except Exception as e:
        return 'Exception while querying elasticsearch: {}'.format(e), 500
    output_array = []
    for hit in result['hits']['hits']:
        output_array.append(hit['_source'])

    return output_array
