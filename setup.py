from distutils.core import setup
import djsphinx

setup(
    name = "djsphinx",
    version = djsphinx.__version__,
    packages = ["djsphinx"],
    url = 'https://github.com/PixxxeL/djsphinx',
    author = 'pixel',
    author_email = 'ivan.n.sergeev@gmail.com',
    maintainer = 'pixel',
    maintainer_email = 'ivan.n.sergeev@gmail.com',
    license = 'GPL3',
    description = 'Sphinx Search Engine integration with Django ORM through Python client for Sphinx by Michael Kurze, James Socol',
    download_url = 'https://github.com/PixxxeL/djsphinx/archive/master.zip',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    #include_package_data = True,
    #install_requires = [
    #    'https://github.com/jsocol/sphinxapi/archive/master.zip'
    #],
)
