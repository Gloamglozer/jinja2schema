#!/usr/bin/env python
import os
import sys
import re

from setuptools import setup, find_packages


__version__ = ''
with open('jinja2schema/__init__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break


if not __version__:
    raise RuntimeError('Cannot find version information')


if sys.argv[-1] in ('submit', 'publish'):
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='jinja2schema',
    version=__version__,
    description='Type inference for Jinja2 templates.',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='Anton Romanovich',
    author_email='anthony.romanovich@gmail.com',
    url='https://jinja2schema.readthedocs.io',
    packages=find_packages(exclude=['tests']),
    install_requires=['Jinja2>=2.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
