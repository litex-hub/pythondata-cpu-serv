import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.2.0.post143"
version_tuple = (1, 2, 0, 143)
try:
    from packaging.version import Version as V
    pversion = V("1.2.0.post143")
except ImportError:
    pass

# Data version info
data_version_str = "1.2.0.post1"
data_version_tuple = (1, 2, 0, 1)
try:
    from packaging.version import Version as V
    pdata_version = V("1.2.0.post1")
except ImportError:
    pass
data_git_hash = "5cc7b0cbe19ae9b02e3c778b5d2f9cb75b9d9eb4"
data_git_describe = "1.2.0-1-g5cc7b0c"
data_git_msg = """\
commit 5cc7b0cbe19ae9b02e3c778b5d2f9cb75b9d9eb4
Author: Eric Brombaugh <ebrombaugh1@cox.net>
Date:   Mon Aug 8 12:17:56 2022 -0700

    Guarantee at least 2 cycles of o_rst after PLL locked.

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
