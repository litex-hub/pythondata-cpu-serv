import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post145"
version_tuple = (1, 1, 0, 145)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post145")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post28"
data_version_tuple = (1, 1, 0, 28)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post28")
except ImportError:
    pass
data_git_hash = "e59fe5346aabc555b8ed21b4e09eb14015340e6b"
data_git_describe = "1.1.0-28-ge59fe53"
data_git_msg = """\
commit e59fe5346aabc555b8ed21b4e09eb14015340e6b
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Mon Jan 3 18:12:48 2022 +0100

    Refactor docs and add interface documentation

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
