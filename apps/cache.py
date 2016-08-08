# -*- encoding: utf-8 -*-

from werkzeug.contrib.cache import MemcachedCache, SimpleCache


class BinarySupportedMemcachedCache(MemcachedCache):
    def import_preferred_memcache_lib(self, servers):
        import pylibmc
        return pylibmc.Client(servers, binary=True)


def make(enabled_memcached, timeout, servers):
    if enabled_memcached:
        return BinarySupportedMemcachedCache(
                servers,
                default_timeout=timeout
                )
    else:
        return SimpleCache(default_timeout=timeout)
