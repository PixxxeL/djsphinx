import sys

try:
    from django.conf import settings
except ImportError:
    settings = object()

py_ver = sys.version_info
if py_ver[0] > 2:
    from .sphinxapi_py3 import *
else:
    from .sphinxapi import *


TOTAL_LIMIT = 10000


def sphinx_search(query_str, index=None, offset=0, limit=TOTAL_LIMIT):
    host = getattr(settings, 'SPHINX_HOST', '127.0.0.1')
    port = getattr(settings, 'SPHINX_PORT', 9312)
    index = index or getattr(settings, 'SPHINX_DEFAULT_INDEX', 'index_name')
    cl = SphinxClient()
    cl.SetServer(host, port)
    cl.SetMatchMode(SPH_MATCH_ALL)
    cl.SetLimits(offset, limit)
    res = cl.Query(query_str, index)
    if res and 'matches' in res:
        return list(map(lambda m: m['id'], res['matches']))
    else:
        return []
