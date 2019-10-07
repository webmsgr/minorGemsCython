
import glob, os, sys

import CppHeaderParser

template = """cdef extern from '{}':
    pass\n"""
fil = open("minorGemsWrapper.pxd","w")
for filename in glob.iglob('minorGems/**', recursive=True):
    if os.path.isfile(filename) and filename.endswith(".h"): # filter dirs
        fil.write(template.format(filename)) # print all files
fil.close()

def include(file):
    try:
        cppHeader = CppHeaderParser.CppHeader(file)
    except CppHeaderParser.CppParseError as e:
        print(e)
        sys.exit(1)
