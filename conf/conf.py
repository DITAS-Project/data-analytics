import os
import json


if os.path.isfile('/opt/blueprint/blueprint.json') and os.path.isfile('/etc/ditas/vdc/data-analytics.json'):
    with open('/opt/blueprint/blueprint.json', 'r') as blueprint_cont:
        try:
            blueprint = json.load(blueprint_cont)
        except Exception as e:
            print('Could not load JSON content from blueprint file: {}'.format(e))
    with open('/etc/ditas/vdc/data-analytics.json') as da_conf_file:
        try:
            da_conf = json.load(da_conf_file)
        except Exception as e:
            print('Could not load JSON content from config file: {}'.format(e))

    config = dict()
    config['infra_names'] = []
    config['infra'] = {}
    for infra in blueprint['COOKBOOK_APPENDIX']['infrastructure']:
        config['infra_names'].append(infra['name'])
        config['infra'][infra['name']] = {}
        for res in infra['resources']:
            config['infra'][infra['name']][res['name']] = {}
            config['infra'][infra['name']][res['name']]['cpu'] = res['cpu']

    config['es_api'] = da_conf['ElasticSearchURL']
    config['port'] = da_conf['Port']
    config['k8s_metrics'] = da_conf['K8s_metrics']
else:
    CONFIG_LOCATION = os.getenv('DA_CONFIG',
                                os.path.join(os.path.expanduser('~'), '.data-analytics.conf')
                                )

    from configobj import ConfigObj

    config = ConfigObj(CONFIG_LOCATION)
