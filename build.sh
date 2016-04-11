#!/bin/bash
ln -s . mookoo
python setup.py sdist
rm mookoo
rm -rf build *.egg-info