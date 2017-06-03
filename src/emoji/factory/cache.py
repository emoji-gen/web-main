# -*- encoding: utf-8 -*-

from werkzeug.contrib.cache import MemcachedCache, SimpleCache

from emoji import app

class BinarySupportedMemcachedCache(MemcachedCache):
    def import_preferred_memcache_lib(self, servers):
        import pylibmc
        return pylibmc.Client(servers, binary=True)

def make_cache():
    timeout = app.config['CACHE_TIMEOUT']
    if app.config['MEMCACHED_ENABLED']:
        hosts = app.config['MEMCACHED_HOSTS']
        return BinarySupportedMemcachedCache(hosts, default_timeout=timeout)

    return SimpleCache(default_timeout=timeout)
