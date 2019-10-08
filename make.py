
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
    for i in glob.iglob("./build/minorGems/**/*.cpp",recursive=True):
        if "win32" in i or "linux" in i or "example" in i or "3d" in i:
            continue
        with open("{}/__init__.py".format(os.path.dirname(i)),"w"):
            pass
        inp = i.split(".h")[0]
        print("converting {0}.cpp to {0}.xml".format(inp))
        os.system("gccxml {0}.cpp -fxml={0}.xml".format(inp))

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
