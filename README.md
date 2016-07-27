# Django Sphinx Search

Sphinx Search Engine integration with Django ORM
through Python client for Sphinx by Michael Kurze, James Socol
https://github.com/jsocol/sphinxapi

Install by PIP:

```shell
pip install djsphinx
```

Add to settings.py:

```python
INSTALLED_APPS += ['djsphinx']

SPHINX_HOST = '127.0.0.1'
SPHINX_PORT = 9312
```

Set manager for any your model:

```python
from djsphinx import SphinxManager

class AnyModel(models.Model):
    objects = SphinxManager(index='some_sphinx_index_name')
```

Usa like this:

```python
AnyModel.objects.search('what you want to search')
# or
AnyModel.objects.search('what you want to search', 'other_sphinx_index_name')
```
