
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
        inp = ".h".join(i.split(".h")[:-1])
        addit = False
        if inp in catch:
            continue
        else:
            catch.append(inp)
        if (os.path.basename(inp) + ".cpp").lower() in map(str.lower,os.listdir(os.path.dirname(i))):
            addit = True
        with open(inp+"_wrapper.pxd","w") as f:
            print("creating {}_wrapper.pxd".format(inp))
            f.write(include(inp,addit))
    print("creating minorGems_wrapper.pxd")
    with open("build/minorGems_wrapper.pxd","w") as w:
        w.write('\n'.join(["cimport {}".format(x.split("build/")[1].replace("/",".").replace(".pxd","")) for x in glob.glob("build/minorGems/**/*.pxd",recursive=True)]))
    print("creating minorGems.pyx")
    with open("build/minorGems.pyx","w") as w:
        w.write("cimport minorGems_wrapper as minorGems")
    print("creating setup.py")
    with open("build/setup.py","w") as w:
        w.write("""from distutils.core import setup\nfrom Cython.Build import cythonize\nsetup(\n\n    ext_modules = cythonize("minorGems.pyx",language="c++",include_dirs=["""+','.join([x for x in glob.glob("./build/minorGems/**",recursive=True) if os.path.isdir(x)])+"""])\n)""")

funcwrappers = []
def functin(function):
    function['returns'] = function['returns'] if function['returns'] != "void" else ""
    out = "    {}{}{}{} (".format(function['returns'],("*" if function['returns_pointer'] else "")," " if function['returns'] != "" else "",function["name"])
    return out
def include(file,addit=False):
    if addit:
        out = "cdef extern from '{}.cpp':\n    pass\n".format(file)
    else:
        out = ""
    out += "cdef extern from '{}.h':\n".format(file)
    try:
        cppHeader = CppHeaderParser.CppHeader(file+".h")
    except CppHeaderParser.CppParseError as e:
        print("Error parsing {}.h".format(file))
        return ""
    for function in cppHeader.functions:

        out += functin(function)
        params = []
        for param in function['parameters']:
            params.append("{}{}{}".format(param['type'] if param['type'] != "void" else "",("" if "*" in param['type'] else " "),param['name']))
        out += ",".join(params)
        out += ") except +\n"
    for cppclass in cppHeader.classes:
        out += "    ctypedef struct {}:\n".format(cppclass)
        for function in cppHeader.classes[cppclass]["methods"]["public"]:
            out += "    "+functin(function)
            params = []
            for param in function['parameters']:
                params.append("{}{}{}".format(param['type'] if param['type'] != "void" else "",("" if "*" in param['type'] else " "),param['name']))
            out += ",".join(params)
            out += ") except +\n"
    if out == "cdef extern from '{}.h':\n".format(file):
        out += "    pass"
    return out
if __name__ == "__main__":
    main()
