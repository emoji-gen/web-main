# -*- encoding: utf-8 -*-

import yaml
from pathlib import Path

def load_config():
    project_path = str(Path(__file__).resolve().parents[2])
    assets_path = str(Path(project_path).joinpath('assets'))
    templates_path = str(Path(project_path).joinpath('templates'))
    fonts_path = str(Path(project_path).joinpath('resources/fonts'))
    config_path = str(Path(project_path).joinpath('config'))

    default_config_path = str(Path(config_path).joinpath('default.yml'))
    default_config = yaml.full_load(open(default_config_path, 'r', encoding='utf-8'))
    local_config_path = str(Path(config_path).joinpath('local.yml'))
    try:
        local_config = yaml.full_load(open(local_config_path, 'r', encoding='utf-8'))
    except FileNotFoundError:
        local_config = {}

    config = {}
    if isinstance(default_config, dict):
        config.update(default_config)
    if isinstance(local_config, dict):
        config.update(local_config)

    # config/assets.yml
    assets_config_path = str(Path(config_path).joinpath('assets.yml'))
    try:
        assets_config = yaml.full_load(open(assets_config_path, 'r', encoding='utf-8'))
    except FileNotFoundError:
        assets_config = None
    if isinstance(assets_config, dict):
        config.update(assets_config)

    config['project_path'] = project_path
    config['assets_path'] = assets_path
    config['templates_path'] = templates_path
    config['config_path'] = config_path

    return config


