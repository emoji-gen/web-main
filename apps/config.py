# -*- encoding: utf-8 -*-

import os
import yaml

# 'development' or 'production'
env   = os.getenv('FLASK_ENV', 'development')
debug = env == 'development'

# 'config/development.py' or $FLASK_CONFIG_PATH
config_path = os.getenv(
    'FLASK_CONFIG_PATH',
    os.path.join(os.path.dirname(__file__), '../config/development.yml')
    )

# bundled JavaScript path
js_min_path = os.path.join(os.path.dirname(__file__), '../static/js/bundle.min.js')

# configs from YAML file
_config = yaml.load(open(config_path, 'r'))

cache_timeout     = _config['cache']['timeout']
memcached_enabled = _config['cache']['memcached']['enabled']
memcached_servers = _config['cache']['memcached']['servers']

fonts_list = {
    'notosans-mono-bold': {
        'name':'Noto Sans Mono CJK Bold',
        'file':'NotoSansMonoCJKjp-Bold.otf'
    },
    'migu-1m-bold': {
        'name':'Migu 1m bold',
        'file':'migu-1m-bold.ttf'
    },
    'mplus-1p-black': {
        'name':'M+ 1p black',
        'file':'mplus-1p-black.ttf'
    },
    'aoyagireisyoshimo': {
        'name':'青柳隷書しも',
        'file':'aoyagireisyosimo_otf_2_01.otf'
    },
    'rounded-x-mplus-1p-black':{
        'name':'Rounded M+ 1p black',
        'file':'rounded-x-mplus-1p-black.ttf'
    }
}
