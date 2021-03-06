#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
    setup
except ImportError:
    from distutils.core import setup
    setup

from codecs import open
from os import path

setup(
    name='svo_filters',
    version='0.1.17',
    description='A Python wrapper for the SVO Filter Profile Service',
    url='https://github.com/hover2pi/svo_filters',
    author='Joe Filippazzo',
    author_email='jfilippazzo@stsci.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    keywords='astrophysics',
    packages=find_packages(exclude=['contrib', 'docs']),
    package_data={'svo_filters':['data/*','data/filters/*']},
    include_package_data=True,
    install_requires=['numpy','astropy','matplotlib'],

)