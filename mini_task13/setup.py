from setuptools import setup, Extension

module = Extension('foreign', sources=['foreign.c'])

setup(name='foreign',
      version='1.0',
      description='C extension for matrix power',
      ext_modules=[module])
