import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post265"
version_tuple = (1, 0, 265)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post265")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post152"
data_version_tuple = (1, 0, 152)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post152")
except ImportError:
    pass
data_git_hash = "28953fec4c02314f17f78c5666915a43851995fe"
data_git_describe = "v1.0-152-g28953fe"
data_git_msg = """\
commit 28953fec4c02314f17f78c5666915a43851995fe
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Fri Oct 8 22:42:02 2021 +0200

    Simplify shift_op signal

"""

# Tool version info
tool_version_str = "0.0.post113"
tool_version_tuple = (0, 0, 113)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post113")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
