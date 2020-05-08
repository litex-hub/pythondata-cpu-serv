import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post70"
version_tuple = (1, 0, 70)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post70")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post19"
data_version_tuple = (1, 0, 19)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post19")
except ImportError:
    pass
data_git_hash = "794748dac4d318643e6b360b08d83a332cc6b7fd"
data_git_describe = "v1.0-19-g794748d"
data_git_msg = """\
commit 794748dac4d318643e6b360b08d83a332cc6b7fd
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Wed May 6 20:51:55 2020 +0200

    Add support for LX9 Microboard

"""

# Tool version info
tool_version_str = "0.0.post51"
tool_version_tuple = (0, 0, 51)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post51")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
