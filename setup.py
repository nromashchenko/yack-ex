"""
Setuptools script
"""

import os
from setuptools import setup, Extension

os.environ["CC"] = "g++"
os.environ["CFLAGS"] = '-O3 -Wall -std=c++11'

setup(
    install_requires=[
        'biopython==1.70',
        'click==6.7',
        'numpy==1.13.3',
        'yack==0.1'
    ],
    ext_modules = [Extension(".jsd", ["jsd.cpp"], language='c++')],
)
