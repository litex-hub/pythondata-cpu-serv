import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.2.0.post142"
version_tuple = (1, 2, 0, 142)
try:
    from packaging.version import Version as V
    pversion = V("1.2.0.post142")
except ImportError:
    pass

# Data version info
data_version_str = "1.2.0.post0"
data_version_tuple = (1, 2, 0, 0)
try:
    from packaging.version import Version as V
    pdata_version = V("1.2.0.post0")
except ImportError:
    pass
data_git_hash = "cb4276e8b23c761389e70221e5cf0bf5ae3ccb91"
data_git_describe = "1.2.0-0-gcb4276e"
data_git_msg = """\
commit cb4276e8b23c761389e70221e5cf0bf5ae3ccb91
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Tue Jul 26 01:19:28 2022 +0200

    Prepare for release

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
