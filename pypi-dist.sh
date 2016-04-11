#!/bin/bash
fm -rf dist build *.egg-info
ln -s . mookoo
python setup.py sdist
rm mookoo
twine upload dist/*
rm -rf dist build *.egg-info