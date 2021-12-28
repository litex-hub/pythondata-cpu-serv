import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post138"
version_tuple = (1, 1, 0, 138)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post138")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post21"
data_version_tuple = (1, 1, 0, 21)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post21")
except ImportError:
    pass
data_git_hash = "7765567cf1f717b7eccadca9c85b5e82e5f21616"
data_git_describe = "1.1.0-21-g7765567"
data_git_msg = """\
commit 7765567cf1f717b7eccadca9c85b5e82e5f21616
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Wed Dec 29 00:17:00 2021 +0100

    Add missing gate on mem_rd with CSR disabled

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
