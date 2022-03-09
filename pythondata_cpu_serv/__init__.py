import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post159"
version_tuple = (1, 1, 0, 159)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post159")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post33"
data_version_tuple = (1, 1, 0, 33)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post33")
except ImportError:
    pass
data_git_hash = "7d08abb92d405b9416f9d7a77fdaba8ba0f52acb"
data_git_describe = "1.1.0-33-g7d08abb"
data_git_msg = """\
commit 7d08abb92d405b9416f9d7a77fdaba8ba0f52acb
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Wed Mar 9 20:59:53 2022 +0100

    Improve makehex.py

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
