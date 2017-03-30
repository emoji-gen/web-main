# -*- encoding: utf-8 -*-

import os
import yaml

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

JSON_AS_ASCII = False

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/emoji?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEFAULT_FONT_KEY = 'mplus-1p-black'
DEFAULT_TEXT = '絵文字。'
DEFAULT_COLOR = '000000FF'
DEFAULT_BACK_COLOR = 'FFFFFF00'

FONT_LIST = _config['fonts']
