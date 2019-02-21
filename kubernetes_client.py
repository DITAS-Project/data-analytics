import re
import json
import requests

from kubernetes import client
from .conf import config


class GenericK8Client:

    def __init__(self, infra_name=None, host=None, api_key=None, verify_ssl=False, **kwargs):
        self.host = host if host is not None else config['infra'][infra_name]['host']
        if 'api_key' in config:
            self.api_key = config['api_key']
        else:
            self.api_key = api_key
        if 'verify_ssl' in config:
            self.verify_ssl = config['verify_ssl']
        else:
            self.verify_ssl = verify_ssl
        self.client_kwargs = kwargs

    def client_conf(self):
        c = client.Configuration()
        c.host = self.host
        if self.api_key:
            c.api_key = {"authorization": "Bearer " + self.api_key}
        c.verify_ssl = self.verify_ssl
        for k, v in self.client_kwargs.items():
            setattr(c, k, v)

        return c

    def custom_client(self, path):
        client_config = self.client_conf()
        api_client = client.ApiClient(client_config)
        result = api_client.call_api(path, 'GET', auth_settings=['BearerToken'], _preload_content=False)
        return json.loads(result[0].data.decode('utf-8'))

    def v1client(self):
        client_config = self.client_conf()
        api_client = client.ApiClient(client_config)
        v1 = client.CoreV1Api(api_client)
        return v1


class HeketiClient:

    def __init__(self, infra_name=None, host=None, user=None, key=None, verify=False):
        self.host = host if host is not None else config['infra'][infra_name]['host']
        self.user = user
        self.key = key
        self.verify = verify

    def client(self, path, method, data={}, headers={}):

        r = requests.request(method, self.host + path, headers=headers, data=json.dumps(data), verify=self.verify)
        r.raise_for_status()
        return r

    def get_storage_metrics(self, substring='free'):

        r = requests.request('GET', self.host + '/api/v1/namespaces/kube-system/services/heketi:8080/proxy/metrics',
                             verify=self.verify)
        r.raise_for_status()

        devices = re.findall(r'heketi_device_count{(.*?)} (\d+)', r.content.decode('utf-8'))
        storage_nodes_count = len(devices)
        device_count = devices[0][1]
        bytes_regex = r'heketi_device_' + substring + r'_bytes{(.*?)} (\d.\d*[e]\W\d*)'
        bytes_free_list = re.findall(bytes_regex, r.content.decode('utf-8'))

        if len(bytes_free_list) > storage_nodes_count:
            bytes_free = 0
            for i in range(1, int(device_count) + 1):
                bytes_free += float(bytes_free_list[storage_nodes_count * 1][1])
        else:
            bytes_free = float(bytes_free_list[0][1])

        return {'device_count': device_count, 'total_bytes_{}'.format(substring): bytes_free,
                'storage_nodes_count': storage_nodes_count}






