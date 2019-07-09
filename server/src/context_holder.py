# -*- encoding: utf-8 -*-

class ContextHolder():
    context = None

    @classmethod
    def set_context(cls, context):
        cls.context = context
