import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post171"
version_tuple = (1, 1, 0, 171)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post171")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post35"
data_version_tuple = (1, 1, 0, 35)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post35")
except ImportError:
    pass
data_git_hash = "4ddd154b249f46522f164aa9a49cce3edfafe03c"
data_git_describe = "1.1.0-35-g4ddd154"
data_git_msg = """\
commit 4ddd154b249f46522f164aa9a49cce3edfafe03c
Author: Wadood <82087831+Abdulwadoodd@users.noreply.github.com>
Date:   Tue May 17 12:11:56 2022 +0500

    Nexys 2 Board support
    
    Added nexys 2 target support for servant

"""

# Tool version info
tool_version_str = "0.0.post136"
tool_version_tuple = (0, 0, 136)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post136")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
