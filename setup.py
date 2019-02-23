from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='chat',
      version='1.0',
      description='Python Distribution Utilities',
      author='Gilmar P Santos',
      packages=find_packages('.'),
      package_dir={'': '.'},
      py_modules=[splitext(basename(path))[0] for path in glob('./*.py')],
     )
