import json

from swagger_server.util import nodename_sanitizer


with open('/etc/ditas/data-analytics.json') as da_conf_file:
    try:
        da_conf = json.load(da_conf_file)
    except Exception as e:
        print('Could not load JSON content from config file: {}'.format(e))

config = dict()
config['infra_names'] = []
config['infra'] = {}
config['TraefikPort'] = da_conf['TraefikPort']

config['es_api'] = da_conf['ElasticSearchURL']
config['elasticsearch_authenticate'] = da_conf['elasticsearch_authenticate']
config['elasticsearch_user'] = da_conf['elasticsearch_user']
config['elasticsearch_password'] = da_conf['elasticsearch_password']
config['port'] = da_conf['Port']


def get_vdc_config(vdc_id, infra_id=None):
    file_path = '/var/ditas/vdm/DS4M/blueprints/vdc-{}.json'.format(vdc_id)
    with open(file_path, 'r') as blueprint_cont:
        try:
            blueprint = json.load(blueprint_cont)
        except Exception as e:
            print('Could not load JSON content from blueprint file: {}'.format(e))

    for infra in blueprint['COOKBOOK_APPENDIX']['Resources']['infrastructures']:
        config['infra_names'].append(infra['name'])
        config['infra'][infra['name']] = {}
        for res in infra['resources']:
            config['infra'][infra['name']][res['name']] = {}
            config['infra'][infra['name']][res['name']]['cpu'] = res['cpu']
            if res['role'] == 'master':
                if 'ip' in res:
                    config['infra'][infra['name']]['host'] = 'http://{}:{}'.format(res['ip'], config['TraefikPort'])
                else:
                    config['infra'][infra['name']]['host'] = 'http://{}:{}'.format(
                        nodename_sanitizer(infra['name'], res['name']), config['TraefikPort'])

    return config

