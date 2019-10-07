
import glob, os, sys, shutil

import CppHeaderParser

def main():
    print("Creating build dir...")
    try:
        os.mkdir("build")
    except:
        shutil.rmtree("build")
        os.mkdir("build")
    os.mkdir("build/minorGems/")
    print("Copying minorGems directory struture...")
    shutil.copytree("./minorGems","./build/minorGems")
def include(file):
    try:
        cppHeader = CppHeaderParser.CppHeader(file)
    except CppHeaderParser.CppParseError as e:
        print(e)
        sys.exit(1)
if __name__ == "__main__":
    main()
