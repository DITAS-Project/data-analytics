mport os

CONFIG_LOCATION = os.getenv('K8CLIENT_CONFIG',
                            os.path.join(os.path.expanduser('~'), '.k8client.conf')
                            )

from configobj import ConfigObj


config = ConfigObj(CONFIG_LOCATION)
