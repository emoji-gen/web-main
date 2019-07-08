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
    config['fonts_path'] = fonts_path
    config['config_path'] = config_path
    config['htmlmin_enabled'] = True

    return config


class Config():
    def __init__(self):
        self._path_config = PathConfig()
        self._mysql = MySQLConfig()
        self._locales = LocalesConfig(self._path_config)

    @property
    def mysql(self):
        return self._mysql

    @property
    def locales(self):
        return self._locales


class PathConfig():
    def __init__(self):
        self._project_path = Path(__file__).resolve().parents[2]

    @property
    def project_path(self):
        return self._project_path


class MySQLConfig():
    def __init__(self):
        config = load_config()
        self._host = config['mysql']['host']
        self._user = config['mysql']['user']
        self._password = config['mysql']['password']

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return 3306

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password


class LocalesConfig():
    def __init__(self, path_config):
        self._locales_path = path_config.project_path.joinpath('locales')

    @property
    def locales(self):
        return ['ja', 'ko']

    @property
    def locales_path(self):
        return self._locales_path
