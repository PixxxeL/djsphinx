# DONT USE IT! SphinxSearch legacy client wrapper for Django 

Sphinx Search Engine integration with Django ORM
through Python client for Sphinx by Michael Kurze, James Socol
https://github.com/jsocol/sphinxapi

Install by PIP:

```shell
pip install djsphinx
```

Add to `settings.py` optionally:

```python
SPHINX_HOST = '127.0.0.1'
SPHINX_PORT = 9312
SPHINX_DEFAULT_INDEX = 'index_name'
```

Usa like this:

```python
from djsphinx import sphinx_search

sphinx_search('what you want to search')
# or
sphinx_search('what you want to search', index='other_sphinx_index_name')
# you may set offset and limit of request (default - 0 and 10000)
sphinx_search('what you want to search', offset=0, limit=100)
```

`sphinx_search` return list of IDs.
