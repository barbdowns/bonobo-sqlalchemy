# This file is autogenerated by edgy.project code generator.
# All changes will be overwritten.

import os
from setuptools import setup, find_packages

root_dir = os.path.dirname(os.path.abspath(__file__))

tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))

def read(filename, flt=None):
    with open(filename) as f:
        content = f.read().strip()
        return flt(content) if callable(flt) else content

# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:
    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)

version_ns = {}
execfile(os.path.join(root_dir, 'bonobo_sqlalchemy/_version.py'), version_ns)
version = version_ns.get('__version__', 'dev')

setup(
    name = 'bonobo_sqlalchemy',
    description = 'Bonobo SQLAlchemy Extension',
    license = 'Apache License, Version 2.0',
    install_requires = ['bonobo', 'SQLAlchemy >=1.1,<1.2'],
    version = version,
    long_description = read('README.rst'),
    classifiers = read('classifiers.txt', tolines),
    packages = find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data = True,
    extras_require = {'dev': ['coverage >=4.2,<4.3',
         'mock >=2.0,<2.1',
         'nose >=1.3,<1.4',
         'pylint >=1.6,<1.7',
         'pytest >=3,<4',
         'pytest-cov >=2.4,<2.5',
         'sphinx',
         'sphinx_rtd_theme',
         'yapf']},
    url = 'https://bonobo-project.org/',
    download_url = 'https://github.com/python-bonobo/bonobo-sqlalchemy/tarball/{version}'.format(version=version),
)