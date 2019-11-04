from elasticsearch import Elasticsearch, ElasticsearchException
from conf.conf import config


class ElasticClient:

    def __init__(self, es_api=None, **kwargs):
        self.es_api = es_api if es_api and 'es_api' not in config else config['es_api']
        self.es = Elasticsearch(self.es_api, **kwargs)

    def search(self, index_name, query, **kwargs):
        if not self.es.indices.exists(index_name):
            raise ElasticsearchException('Index {} does not exist'.format(index_name))
        res = self.es.search(index=index_name, body=query, **kwargs)
        return res

