#!/bin/sh
# Deploy this library to pypi.

python setup.py sdist
python setup.py register
python setup.py sdist upload
