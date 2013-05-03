#!/usr/bin/env python

from distutils.core import setup

setup(name='pychatjs',
      version='1.0.0.1',
      description='Python chat written using tornado and graceful-websockets',
      author='Noah Hall',
      author_email='enalicho@gmail.com',
      url='http://github.com/AstralDynamics/PyChat.js',
      packages=['pychatjs', 'pychatjs/server'],
     )
