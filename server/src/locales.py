# -*- encoding: utf-8 -*-

import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class Locales():
    def __init__(self, config):
        self._locales = config.locales
        self._locales_path = config.locales_path

    async def startup(self):
        for locale in self._locales:
            locale_path = Path(self._locales_path).resolve().joinpath(locale + ".yml")
            if not locale_path.is_file():
                raise RuntimeError(
                    'A locale file is not found. :: locale={}, path={}'.format(locale, locale_path))

    def get_message(key):
        pass
