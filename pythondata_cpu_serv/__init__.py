import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post86"
version_tuple = (1, 0, 86)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post86")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post26"
data_version_tuple = (1, 0, 26)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post26")
except ImportError:
    pass
data_git_hash = "a742002707de46a685d94b788a26b684542a69a7"
data_git_describe = "v1.0-26-ga742002"
data_git_msg = """\
commit a742002707de46a685d94b788a26b684542a69a7
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Fri Jun 5 15:30:51 2020 +0200

    Add links to movies

"""

# Tool version info
tool_version_str = "0.0.post60"
tool_version_tuple = (0, 0, 60)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post60")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
