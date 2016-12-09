# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name = 'bogosort',
    ext_modules = cythonize('*.pyx'),
    include_dirs = [np.get_include()]
)
