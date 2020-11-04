import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post117"
version_tuple = (1, 0, 117)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post117")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post51"
data_version_tuple = (1, 0, 51)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post51")
except ImportError:
    pass
data_git_hash = "215099dd3d3abc55bf169f9ee592676da1722cb2"
data_git_describe = "v1.0-51-g215099d"
data_git_msg = """\
commit 215099dd3d3abc55bf169f9ee592676da1722cb2
Author: Qingyao Sun <sunqingyao19970825@icloud.com>
Date:   Fri Oct 2 18:01:39 2020 +0800

    Add instructions for iCESugar to README.md

"""

# Tool version info
tool_version_str = "0.0.post66"
tool_version_tuple = (0, 0, 66)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post66")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
