
import glob, os

for filename in glob.iglob('minorGems/**', recursive=True):
    if os.path.isfile(filename) and filename.endswith(".h"): # filter dirs
        print(filename)
