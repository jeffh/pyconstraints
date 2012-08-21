#!/usr/bin/env python
from distutils.core import setup

with open('LICENSE') as h:
    LICENSE = h.read()

with open('README.md') as h:
    README = h.read()

setup(
    name='pyconstraints',
    description='A simple constraints satisfaction solver',
    long_description=README,
    license=LICENSE,
    version='1.0.0',
    author='Jeff Hui',
    author_email='jeff@jeffhui.net',
    url='http://github.com/jeffh/pyconstraints',
    packages=['pyconstraints'],
    requires=[],
)
