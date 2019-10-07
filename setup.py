from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="minorGems",
    ext_modules=cythonize("minorGems.pyx", languge="c++"),
)
