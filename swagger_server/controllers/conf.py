import os
import json

from swagger_server.util import nodename_sanitizer

if os.path.isfile('/opt/blueprint/blueprint.json'):
    with open('/opt/blueprint/blueprint.json', 'r') as blueprint_cont:
        try:
            blueprint = json.load(blueprint_cont)
        except Exception as e:
            print('Could not load JSON content from blueprint file: {}'.format(e))

    config = {}
    config['infra_names'] = []
    config['infra'] = {}
    for infra in blueprint['COOKBOOK_APPENDIX']['infrastructure']:
        config['infra_names'].append(infra['name'])
        config['infra'][infra['name']] = {}
        config['infra'][infra['name']]['node_names'] = []
        for res in infra['resources']:
            config['infra'][infra['name']]['node_names'].append(res['name'])
            if res['role'] == 'master':
                if 'ip' in res:
                    config['infra'][infra['name']]['host'] = 'http://{}:9999'.format(res['ip'])
                else:
                    config['infra'][infra['name']]['host'] = 'http://{}:9999'.format(
                        nodename_sanitizer(infra['name'], res['name']))

else:
    CONFIG_LOCATION = os.getenv('DA_CONFIG',
                                os.path.join(os.path.expanduser('~'), '.data-analytics.conf')
                                )

    from configobj import ConfigObj

    config = ConfigObj(CONFIG_LOCATION)
