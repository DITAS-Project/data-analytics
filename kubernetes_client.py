from kubernetes import client, config
from conf import config


class GenericK8Client:

	def __init__(self, host=None, api_key=None, verify_ssl=False, **kwargs):
		self.host = host if host is not None else config['host']
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
		result = api_client.call_api(path, 'GET', auth_settings = ['BearerToken'], response_type='json', _preload_content=False)
		return result[0].data.decode('utf-8')

	def v1client(self):
		client_config = self.client_conf()
		api_client = client.ApiClient(client_config)
		v1 = client.CoreV1Api(api_client)
		return v1

