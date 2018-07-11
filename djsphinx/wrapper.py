# -*- coding: utf-8 -*-

try:
    from django.conf import settings
except ImportError:
    settings = object()
from .sphinxapi import *

def sphinx_search(query_str, index=None):
    host = getattr(settings, 'SPHINX_HOST', '127.0.0.1')
    port = getattr(settings, 'SPHINX_PORT', 9312)
    index = index or getattr(settings, 'SPHINX_DEFAULT_INDEX', 'index_name')
    cl = SphinxClient()
    cl.SetServer(host, port)
    cl.SetMatchMode(SPH_MATCH_ALL)
    res = cl.Query(query_str, index)
    if res and res.has_key('matches'):
        return map(lambda m: m['id'], res['matches'])
    else:
        return []
