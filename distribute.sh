#!/bin/sh
# Deploy this library to pypi.

python setup.py sdist
python setup.py register
twine upload dist/* #note: must increment version number to have a succesful upload.
