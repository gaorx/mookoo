#!/usr/bin/env python
from setuptools import setup

setup(
    name='mookoo',
    version='0.1.0',
    description="Mock HTTP server",
    author='GaoRongxin',
    author_email='rongxin.gao@gmail.com',
    url='https://github.com/gaorx/mookoo/',
    license='MIT',
    platforms='any',
    packages=['mookoo'],
    package_data={
        '': ['help.html', 'README.md', 'LICENSE'],
    },
    entry_points={
        'console_scripts': ['mookoo = mookoo:cli_entry'],
    }
)
