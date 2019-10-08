import glob
import os
import sys
sys.path.append(os.path.abspath("."))
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
includepath = [x for x in glob.glob("./**",recursive=True) if os.path.isdir(x)]

modules = [Extension("minorGems",["minorGems.pyx"],language="c++",include_path=includepath)]
out = []
for pyx in glob.glob("./minorGems/**/*.pyx",recursive=True):
    modname = os.path.basename(pyx).split(".")[0].replace("_wrapper","")
    out = [Extension(modname,[pyx],language="c++",include_path=includepath)] + out
out += modules
setup(
    ext_modules = cythonize(out)
)