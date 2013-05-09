#!/usr/bin/env python

from distutils.core import setup

setup(name='pychatjs',
      version='1.0.0.6',
      description='Python chat written using tornado and graceful-websockets',
      author='Noah Hall',
      author_email='enalicho@gmail.com',
      url='https://github.com/AstralDynamics/PyChat.js/archive/master.zip',
      packages=['pychatjs', 'pychatjs/server'],
      requires=['tornado'],
     )
