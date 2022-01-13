import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post152"
version_tuple = (1, 1, 0, 152)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post152")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post30"
data_version_tuple = (1, 1, 0, 30)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post30")
except ImportError:
    pass
data_git_hash = "09e49f784a44377e3f9f28fca85c77ab163e03a5"
data_git_describe = "1.1.0-30-g09e49f7"
data_git_msg = """\
commit 09e49f784a44377e3f9f28fca85c77ab163e03a5
Author: somhi <somhix@gmail.com>
Date:   Thu Jan 13 22:39:27 2022 +0100

    added board_device_index : 2 to chameleon96 for programming

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
