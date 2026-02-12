from setuptools import find_packages
from setuptools import setup
import os

root_path = os.path.dirname(__file__)
require = open(os.path.join(root_path, 'requirements.txt')).readlines()

setup(
    name='pymind',
    version='1.0.2',
    url='https://github.com/housenli/pyMIND',
    description='Python implementation of Multiscale Nemirovski Dantzig Estimators',
    packages=find_packages(),
    package_dir={'pymind': 'pymind'},
    author={'Leo Claus Weber', 'Housen Li'},
    install_requires=[require]
)
