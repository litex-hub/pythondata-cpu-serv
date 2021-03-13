import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post192"
version_tuple = (1, 0, 192)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post192")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post97"
data_version_tuple = (1, 0, 97)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post97")
except ImportError:
    pass
data_git_hash = "727bb40a8784c50b081abdcfd784a5bc7c34e40e"
data_git_describe = "v1.0-97-g727bb40"
data_git_msg = """\
commit 727bb40a8784c50b081abdcfd784a5bc7c34e40e
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Sun Mar 14 00:12:29 2021 +0100

    Simplify control logic for bool ops

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
