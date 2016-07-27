# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from .sphinxapi import *


class SphinxManager(models.Manager):

    def __init__(self, *args, **kwargs):
        self.sphinx_index = kwargs.get('index')
        assert self.sphinx_index, 'You must define index argument in SphinxManager constructor invokation'
        super(SphinxManager, self).__init__()

    def __getattr__(self, attr, *args):
        try:
            return getattr(SphinxManager, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)

    def get_query_set(self):
        return self.model.QuerySet(self.model)

    def search(self, query, index=None):
        cl = SphinxClient()
        cl.SetServer(settings.SPHINX_HOST, settings.SPHINX_PORT)
        cl.SetMatchMode(SPH_MATCH_ALL)
        res = cl.Query(query, index or self.sphinx_index)
        if res and res.has_key('matches'):
            pks = map(lambda m: m['id'], res['matches'])
        else:
            pks = []
        return self.get_queryset().filter(pk__in=pks)
