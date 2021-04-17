import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post196"
version_tuple = (1, 0, 196)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post196")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post101"
data_version_tuple = (1, 0, 101)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post101")
except ImportError:
    pass
data_git_hash = "f4b75f0be34377643f4cca5614249d2fd01d346b"
data_git_describe = "v1.0-101-gf4b75f0"
data_git_msg = """\
commit f4b75f0be34377643f4cca5614249d2fd01d346b
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Sat Apr 17 23:59:15 2021 +0200

    Start documenting instruction life cycle

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
