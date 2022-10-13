import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.2.0.post145"
version_tuple = (1, 2, 0, 145)
try:
    from packaging.version import Version as V
    pversion = V("1.2.0.post145")
except ImportError:
    pass

# Data version info
data_version_str = "1.2.0.post3"
data_version_tuple = (1, 2, 0, 3)
try:
    from packaging.version import Version as V
    pdata_version = V("1.2.0.post3")
except ImportError:
    pass
data_git_hash = "6ad60f69a20c969ce46a605af9661b224d7e765d"
data_git_describe = "1.2.0-3-g6ad60f6"
data_git_msg = """\
commit 6ad60f69a20c969ce46a605af9661b224d7e765d
Author: gojimmypi <13059545+gojimmypi@users.noreply.github.com>
Date:   Thu Dec 23 12:10:43 2021 -0800

    Add ICE-V Wireless support

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
