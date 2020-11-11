import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post126"
version_tuple = (1, 0, 126)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post126")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post60"
data_version_tuple = (1, 0, 60)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post60")
except ImportError:
    pass
data_git_hash = "90ce4ff1afd1ec84817f3c4284f98f1cbbed97ad"
data_git_describe = "v1.0-60-g90ce4ff"
data_git_msg = """\
commit 90ce4ff1afd1ec84817f3c4284f98f1cbbed97ad
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Tue Nov 10 15:13:04 2020 +0100

    Syntax and reset fixes for ModelSim

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
