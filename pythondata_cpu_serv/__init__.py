import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post178"
version_tuple = (1, 1, 0, 178)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post178")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post36"
data_version_tuple = (1, 1, 0, 36)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post36")
except ImportError:
    pass
data_git_hash = "2655861447054d37b032795dcedc0fecf1d49dc3"
data_git_describe = "1.1.0-36-g2655861"
data_git_msg = """\
commit 2655861447054d37b032795dcedc0fecf1d49dc3
Author: Abd <abdulwadood.afzal88@gmail.com>
Date:   Wed Mar 23 15:21:58 2022 +0500

    Compressed Extension for SERV

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
