import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post177"
version_tuple = (1, 0, 177)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post177")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post92"
data_version_tuple = (1, 0, 92)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post92")
except ImportError:
    pass
data_git_hash = "bc9705bef2a8e1f21b0df7f8a59cc8541851e811"
data_git_describe = "v1.0-92-gbc9705b"
data_git_msg = """\
commit bc9705bef2a8e1f21b0df7f8a59cc8541851e811
Author: somhi <jordisx@gmail.com>
Date:   Sat Jan 30 12:52:38 2021 +0100

    add support for SoCKit development kit board

"""

# Tool version info
tool_version_str = "0.0.post85"
tool_version_tuple = (0, 0, 85)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post85")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
