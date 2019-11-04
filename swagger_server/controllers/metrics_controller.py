from swagger_server.models.metric_res import MetricRes  # noqa: E501
from swagger_server import util

from conf.conf import config
from clients.elastic_client import ElasticClient


BASE_QUERY = {
  "_source": ["meter.name", "meter.operationID", "meter.value", "meter.unit", "meter.timestamp", "meter.appendix"],
  "query": {
    "bool": {
      "must": [{
        "exists": {"field": "meter"}
        },
        {
          "match": {
            "meter.name": ""
          }
        },
        {
          "match": {
            "meter.operationID": ""
          }
        },
        {
          "range": {
            "meter.timestamp": {
              "gte": "",
              "lt": ""
            }
          }
        }
      ]
    }
  }
}


def getmetrics(infraId, operationID, name, startTime, endTime):  # noqa: E501

    """getmetrics

    Get metric value based on meter operation id, name, timestamp # noqa: E501

    :param infraId: The infrastructure name based on the blueprint
    :type infraId: str
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

    if infraId not in config['infra_names']:
        return 'Infrastructure Id not found in Blueprint', 404

    startTime = util.deserialize_datetime(startTime)
    endTime = util.deserialize_datetime(endTime)
    index_name = '{}-*'.format(infraId)
    BASE_QUERY['query']['bool']['must'][1]['match']['meter.name'] = name
    BASE_QUERY['query']['bool']['must'][2]['match']['meter.operationID'] = operationID
    BASE_QUERY['query']['bool']['must'][3]['range']['meter.timestamp']['gte'] = startTime
    BASE_QUERY['query']['bool']['must'][3]['range']['meter.timestamp']['lt'] = endTime

    es = ElasticClient()
    try:
        result = es.search(index_name, query=BASE_QUERY)
    except Exception as e:
        return 'Exception while querying elasticsearch: {}'.format(e), 500
    output_array = []
    for hit in result['hits']['hits']:
        output_array.append(hit['_source'])

    return output_array
