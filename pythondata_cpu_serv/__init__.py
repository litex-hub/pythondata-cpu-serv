import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post180"
version_tuple = (1, 1, 0, 180)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post180")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post38"
data_version_tuple = (1, 1, 0, 38)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post38")
except ImportError:
    pass
data_git_hash = "a8f7de9e8c57227fcd187a685193148094bd3fc0"
data_git_describe = "1.1.0-38-ga8f7de9"
data_git_msg = """\
commit a8f7de9e8c57227fcd187a685193148094bd3fc0
Author: Abd <abdulwadood.afzal88@gmail.com>
Date:   Tue May 31 03:36:35 2022 +0500

    compressed parameter added for Nexys-2 FPGA target

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
