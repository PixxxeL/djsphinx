try:
    from .model_manager import SphinxManager
except ImportError:
    pass

VERSION = (0, 0, 3,)
__version__ = '.'.join(map(str, VERSION))
