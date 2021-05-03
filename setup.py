#!/usr/bin/env python

from distutils.core import setup

with open('README.md') as f:
    long_description = f.read()

setup(
	name='REPIC',
	version='1.1',
	description='Read Evaluate Print in Comments',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='David Pinney',
	author_email='david@pinney.org',
	url='https://github.com/dpinney/REPIC/',
	py_modules=['REPIC']
)