from __future__ import with_statement
from __future__ import absolute_import
from setuptools import setup, find_packages
from os import path
from lokalise._version import __version__
from io import open


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, u'README.md'), encoding=u'utf-8') as f:
    long_description = f.read()

setup(
    name=u"python-lokalise-api",
    version=__version__,
    author=u"Ilya Bodrov",
    author_email=u"bodrovis@protonmail.com",
    description=u"Official Python interface for the Lokalise API v2",
    long_description=long_description,
    long_description_content_type=u"text/markdown",
    url=u"https://github.com/lokalise/python-lokalise-api",
    keywords=u'lokalise api client',
    license=u'MIT',
    packages=find_packages(exclude=[u'tests*']),
    package_dir={u'lokalise': u'lokalise'},
    platforms=[u'Any'],
    install_requires=[u'requests>2,<3'],
    tests_require=[u'pytest', u'vcrpy', u'pytest-vcr', u'pytest-cov'],
    classifiers=[
        u'Development Status :: 5 - Production/Stable',
        u"Intended Audience :: Developers",
        u"Topic :: Software Development :: Libraries :: Python Modules",
        u"Programming Language :: Python :: 2",
        u"License :: OSI Approved :: BSD License",
        u"Operating System :: OS Independent",
    ],
    python_requires=u'>=2.7',
)
