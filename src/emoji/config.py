# -*- encoding: utf-8 -*-

import yaml
from pathlib import Path

# _config_path = \
#     os.path.join(os.path.dirname(__file__), '../../config/common.yml')
# _env_config_path = os.getenv(
#     'FLASK_CONFIG_PATH',
#     os.path.join(os.path.dirname(__file__), '../../config/development.yml')
#     )

# _config     = yaml.load(open(_config_path, 'r', encoding='utf-8'))
# _env_config = yaml.load(open(_env_config_path, 'r', encoding='utf-8'))


def setup_config(app):
    project_path = str(Path(__file__).resolve().parents[2])
    templates_path = str(Path(project_path).joinpath('templates'))
    fonts_path = str(Path(project_path).joinpath('externals/fonts'))
    config_path = str(Path(project_path).joinpath('config'))

    default_config_path = str(Path(config_path).joinpath('default.yml'))
    default_config = yaml.load(open(default_config_path, 'r', encoding='utf-8'))

    config = {}
    config.update(default_config)
    config['project_path'] = project_path
    config['templates_path'] = templates_path
    config['fonts_path'] = fonts_path
    config['config_path'] = config_path
    config['htmlmin_enabled'] = True

    app['config'] = config
