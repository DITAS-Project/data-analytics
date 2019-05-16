from elasticsearch import Elasticsearch, ElasticsearchException
from .conf import config


class ElasticClient:

    def __init__(self, es_api, **kwargs):
        self.es_api = es_api if 'es_api' not in config else config['es_api']
        self.es = Elasticsearch(self.es_api, **kwargs)

    def search(self, index_name, query, **kwargs):
        if not self.es.indices.exists(index_name):
            raise ElasticsearchException('Index {} does not exist'.format(index_name))
        self.es.search(index=index_name, query=query, **kwargs)

