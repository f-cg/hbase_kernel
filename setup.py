#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
    ['bash_kernel']

package_data = \
    {'': ['*']}

install_requires = \
    ['pexpect>=4.0']

setup(name='bash_kernel',
      version='0.7.2',
      description='A bash kernel for Jupyter',
      author='Thomas Kluyver',
      author_email='thomas@kluyver.me.uk',
      url='https://github.com/takluyver/bash_kernel',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      )
