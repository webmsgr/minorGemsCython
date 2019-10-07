
import glob, os
template = """cdef extern from '{}':
    pass\n"""
fil = open("minorGems.pxd","w")
for filename in glob.iglob('minorGems/**', recursive=True):
    if os.path.isfile(filename) and filename.endswith(".h"): # filter dirs
        fil.write(template.format(filename)) # print all files
fil.close()
