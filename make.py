
import glob, os, sys, shutil

import CppHeaderParser

def main():
    print("Creating build dir...")
    try:
        os.mkdir("build")
    except:
        shutil.rmtree("build")
        os.mkdir("build")
    print("Copying minorGems directory struture...")
    shutil.copytree("./minorGems","./build/minorGems")
    catch = []
    for i in glob.iglob("./build/minorGems/**/*.h",recursive=True):
        if "win32" in i or "linux" in i or "example" in i or "3d" in i:
            continue
        with open("{}/__init__.py".format(os.path.dirname(i)),"w"):
            pass
        inp = i.split(".h")[0]
        print("wrapping {0}.h to {0}_wrapper.pxd".format(inp))
        print("THIS DOES NOT WORK! WORK IN PROGRESS!")

    print("creating minorGems_wrapper.pxd")
    with open("build/minorGems_wrapper.pxd","w") as w:
        w.write('\n'.join(["cimport {}".format(x.split("build/")[1].replace("/",".").replace(".pxd","")) for x in glob.glob("build/minorGems/**/*.pxd",recursive=True)]))
    print("creating minorGems.pyx")
    with open("build/minorGems.pyx","w") as w:
        w.write("cimport minorGems_wrapper")
    print("creating setup.py")
    shutil.copyfile("setup_template.py","build/setup.py")


if __name__ == "__main__":
    main()
