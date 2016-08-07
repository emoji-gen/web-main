import os
import yaml

# 'development' or 'production'
env = os.getenv('FLASK_ENV', 'development')

# 'config/development.py' or $FLASK_CONFIG_PATH
config_path = os.getenv(
    'FLASK_CONFIG_PATH',
    os.path.join(os.path.dirname(__file__), '../config/development.yml')
    )

_config = yaml.load(open(config_path, 'r'))

cache_timeout     = _config['cache']['timeout']
memcached_enabled = _config['cache']['memcached']['enabled']
memcached_servers = _config['cache']['memcached']['servers']
