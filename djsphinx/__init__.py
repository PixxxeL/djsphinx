try:
    from .wrapper import sphinx_search
except ImportError:
    pass

VERSION = (0, 0, 9,)
__version__ = '.'.join(map(str, VERSION))
