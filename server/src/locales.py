# -*- encoding: utf-8 -*-

import yaml
from pathlib import Path


class Locales():
    def __init__(self, config):
        self._locales = config.locales
        self._locales_path = Path(config.locales_path).resolve()
        self._messages = {}


    async def startup(self):
        for locale in self._locales:
            locale_path = self._locales_path.joinpath(locale + '.yml')
            if not locale_path.is_file():
                raise RuntimeError(
                    'A locale file is not found. :: locale={}, path={}'.
                        format(locale, locale_path))

            with open(str(locale_path), 'r', encoding='utf-8') as fp:
                messages = yaml.full_load(fp)
                self._messages[locale] = messages

        self._validate_messages()


    def _validate_messages(self):
        message_keys = set()
        for messages in self._messages.values():
            message_keys.update(messages.keys())

        for (locale, messages) in self._messages.items():
            if message_keys != set(messages.keys()):
                raise RuntimeError(
                    'There is a key that does not exist. :: locale={}, difference={}'.
                        format(locale, message_keys - set(messages.keys())))


    def get_message(*, locale, key):
        if key not in self._messages:
            raise RuntimeError(
                'Illegal message key. :: locale={}, key={}'.format(locale, key))

        return self._messages[key]
