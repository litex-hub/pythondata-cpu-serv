import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post144"
version_tuple = (1, 1, 0, 144)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post144")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post27"
data_version_tuple = (1, 1, 0, 27)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post27")
except ImportError:
    pass
data_git_hash = "a121b19ec45599fa591884767a6bb468772a1c24"
data_git_describe = "1.1.0-27-ga121b19"
data_git_msg = """\
commit a121b19ec45599fa591884767a6bb468772a1c24
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Sun Jan 2 23:52:07 2022 +0100

    Document shift operations

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
