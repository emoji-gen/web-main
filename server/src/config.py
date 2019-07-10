# -*- encoding: utf-8 -*-

from pathlib import Path

import yaml


class Config():
    def __init__(self, *, is_dev):
        self.path_config = PathConfig()
        self.fonts_config = FontsConfig(path_config=self.path_config)
        self.mysql_config = MySQLConfig(path_config=self.path_config, is_dev=is_dev)
        self.locales_config = LocalesConfig(path_config=self.path_config)


# ---------------------------------------------------------
# Fonts
# ---------------------------------------------------------

class FontsConfig():
    def __init__(self, *, path_config):
        self.fonts_path = path_config.externals_path.joinpath('fonts')

        config_path = path_config.config_path.joinpath('fonts.yml')
        with open(config_path, 'r', encoding='utf-8') as fp:
            self._fonts = yaml.full_load(fp)

    def by_locale(self, locale):
        if locale not in self._fonts:
            raise RuntimeError('Not supported locale. :: locale={}'.format(locale))
        return self._fonts[locale]


# ---------------------------------------------------------
# Path
# ---------------------------------------------------------

class PathConfig():
    def __init__(self):
        self.root_path = Path(__file__).resolve().parents[2]
        self.externals_path = self.root_path.joinpath('externals')
        self.project_path = Path(__file__).resolve().parents[1]
        self.config_path = self.project_path.joinpath('config').resolve()


# ---------------------------------------------------------
# MySQL
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# Locales
# ---------------------------------------------------------

class LocalesConfig():
    def __init__(self, *, path_config):
        self.locales_path = path_config.project_path.joinpath('locales')

    @property
    def locales(self):
        return ['ja', 'ko']
