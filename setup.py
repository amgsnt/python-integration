from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='ci-integration',
      version='1.0',
      description='Python Test',
      author='Gilmar P Santos',
      packages=find_packages('.'),
      package_dir={'': '.'},
      py_modules=[splitext(basename(path))[0] for path in glob('./*.py')],
     )
