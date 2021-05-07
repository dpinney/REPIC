#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
	name='REPIC',
	version='1.3',
	description='Read Evaluate Print in Comments',
	long_description_content_type='text/markdown',
	long_description=long_description,
	author='David Pinney',
	author_email='david@pinney.org',
	url='https://github.com/dpinney/REPIC/',
	py_modules=['REPIC']
)