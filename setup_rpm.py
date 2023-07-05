#-*- coding: utf-8 -*-

"""Polaris setup

By default will install to /opt/polaris, to install to a different folder 
set POLARIS_INSTALL_PREFIX env before running "python3 setup.py install"
"""

import os
import sys
import inspect
import shutil
import setuptools


VERSION = '0.7.0'


def main():
   # setup packages
    setuptools.setup(
        version=VERSION,
        author='Anton Gavrik',    
        name='polaris-gslb',
        description=('An extendable Global Server Load Balancing(GSLB) '
                     'solution, DNS-based traffic manager.'),
        packages = setuptools.find_packages('.'),
        install_requires=[
            'pyyaml',
            'python-memcached', 
            'python-daemon-3K'
        ],
        license='BSD 3-Clause',
        url='https://github.com/polaris-gslb/polaris-gslb',
        download_url=('https://github.com/polaris-gslb/polaris-gslb/tarball/v{}'
                      .format(VERSION)),
        classifiers=[
            'Programming Language :: Python :: 3',
        ]
    )

if __name__ == '__main__':
    main()
