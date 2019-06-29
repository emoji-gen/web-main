# -*- encoding: utf-8 -*-

class ContextHolder():
    _context = None

    @classmethod
    def context(cls):
        return cls._context

    @classmethod
    def set_context(cls, context):
        cls._context = context

