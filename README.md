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
sphinx_search('what you want to search', 'other_sphinx_index_name')
```

`sphinx_search` return list of IDs.
