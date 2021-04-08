import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post195"
version_tuple = (1, 0, 195)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post195")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post100"
data_version_tuple = (1, 0, 100)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post100")
except ImportError:
    pass
data_git_hash = "079a5c4250067a4e0a65cf2aa8daed83f0f233c2"
data_git_describe = "v1.0-100-g079a5c4"
data_git_msg = """\
commit 079a5c4250067a4e0a65cf2aa8daed83f0f233c2
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Thu Apr 8 15:36:11 2021 +0200

    Remove unused wgo register

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
