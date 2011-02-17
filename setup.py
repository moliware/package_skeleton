# -*- coding: utf-8 -*-
from distutils.core import setup

import package

setup(name = 'package',
      version = '1.0',
      description = 'Package skeleton',
      author = package.__author__,
      author_email = package.__email__,
      url = '',
      data_files = [('/etc/package', ['conf/package.conf'])],
      packages = ['package'],
      scripts = ['scripts/execute_package.py']
      )
