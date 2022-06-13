import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post183"
version_tuple = (1, 1, 0, 183)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post183")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post41"
data_version_tuple = (1, 1, 0, 41)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post41")
except ImportError:
    pass
data_git_hash = "302224834b40d8d46bb451e9f991e337d10ce69d"
data_git_describe = "1.1.0-41-g3022248"
data_git_msg = """\
commit 302224834b40d8d46bb451e9f991e337d10ce69d
Author: Inoki <veyx.shaw@gmail.com>
Date:   Sat Mar 19 14:14:32 2022 +0100

    Add description for AX309 board target

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
