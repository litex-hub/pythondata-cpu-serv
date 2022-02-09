import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post156"
version_tuple = (1, 1, 0, 156)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post156")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post32"
data_version_tuple = (1, 1, 0, 32)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post32")
except ImportError:
    pass
data_git_hash = "2bb988b553b810f4be64d07b036da12d84c57d35"
data_git_describe = "1.1.0-32-g2bb988b"
data_git_msg = """\
commit 2bb988b553b810f4be64d07b036da12d84c57d35
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Wed Feb 9 18:15:08 2022 +0100

    Add reset for mie_mtie

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
