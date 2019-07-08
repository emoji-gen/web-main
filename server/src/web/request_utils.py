# -*- encoding: utf-8 -*-

REQUEST_LOCALE_KEY = 'locale'


def set_locale(request, locale):
    request[REQUEST_LOCALE_KEY] = locale

def get_locale(request):
    return request.get(REQUEST_LOCALE_KEY)
