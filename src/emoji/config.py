# -*- encoding: utf-8 -*-

import os
import yaml

# -----------------------------------------------------------------------------

_env = os.getenv('FLASK_ENV', 'development')
if _env not in ['development', 'production']:
    sys.exit('invalid environment: {0}'.format(_env))

_config_path = \
    os.path.join(os.path.dirname(__file__), '../../config/common.yml')
_env_config_path = os.getenv(
    'FLASK_CONFIG_PATH',
    os.path.join(os.path.dirname(__file__), '../../config/development.yml')
    )

_config     = yaml.load(open(_config_path, 'r', encoding='utf-8'))
_env_config = yaml.load(open(_env_config_path, 'r', encoding='utf-8'))

# -----------------------------------------------------------------------------

ENV = _env
DEBUG = _env == 'development'

# bundled JavaScript path
JS_MIN_PATH = \
        os.path.join(os.path.dirname(__file__), '../../static/js/bundle.min.js')

JSON_AS_ASCII = False

# -----------------------------------------------------------------------------

HISTORY_ENABLED = _env_config['history']['enabled']

SQLALCHEMY_DATABASE_URI = _env_config['mysql']['url']
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEFAULT_FONT_KEY = 'mplus-1p-black'
DEFAULT_TEXT = '絵文字。'
DEFAULT_COLOR = '000000FF'
DEFAULT_BACK_COLOR = 'FFFFFF00'

FONT_LIST = _config['fonts']

CACHE_VERSION = _config['cache']['version']
CACHE_TIMEOUT = _env_config['cache']['timeout']

MEMCACHED_ENABLED = _env_config['memcached']['enabled']
MEMCACHED_HOSTS = _env_config['memcached']['hosts']

MYSQL_ENABLED = _env_config['mysql']['enabled']

SITE_BASE_URL = _config['site']['base_url']
SITE_DOMAIN = _config['site']['domain']
SITE_DESCRIPTION = _config['site']['description']

SLACK_ENABLED = _env_config['slack']['enabled']
SLACK_WEBHOOK_URL = _env_config['slack']['webhook_url']

