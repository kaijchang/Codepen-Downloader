#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

setup(
    name='cpen',
    packages=find_packages(),
    version='0.1.2',
    description='Hacky Downloader for Codepens',
    author='Kai Chang',
    author_email='kaijchang@gmail.com',
    url='https://github.com/kajchang/CodePen-Downloader',
    license='MIT',
    long_description=open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'README.md')).read(),
    long_description_content_type="text/markdown",
    install_requires=[open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'requirements.txt')).read().split('\n')[:-1]],
    entry_points={
        'console_scripts': [
            'cpen = cpen.codepen_downloader:main']
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    package_data={'cpen.templates': ['*.html']},
    include_package_data=True
)
