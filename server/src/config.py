# -*- encoding: utf-8 -*-

from pathlib import Path

import yaml


class Config():
    def __init__(self, *, is_dev):
        self._path_config = PathConfig()
        self._mysql_config = MySQLConfig(path_config=self._path_config, is_dev=is_dev)
        self._locales_config = LocalesConfig(self._path_config)

    @property
    def mysql_config(self):
        return self._mysql_config

    @property
    def locales_config(self):
        return self._locales_config


class PathConfig():
    def __init__(self):
        self.project_path = Path(__file__).resolve().parents[1]
        self.config_path = self.project_path.joinpath('config').resolve()


class MySQLConfig():
    def __init__(self, *, path_config, is_dev):
        dev_config_path = path_config.config_path.joinpath('mysql-dev.yml')
        prod_config_path = path_config.config_path.joinpath('mysql-prod.yml')
        config_path = dev_config_path if is_dev else prod_config_path

        with open(config_path, 'r', encoding='utf-8') as fp:
            config = yaml.full_load(fp)

        self.host = config['host']
        self.port = config['port']
        self.user = config['user']
        self.password = config['password']
        self.db = config['db']


class LocalesConfig():
    def __init__(self, path_config):
        self.locales_path = path_config.project_path.joinpath('locales')

    @property
    def locales(self):
        return ['ja', 'ko']
