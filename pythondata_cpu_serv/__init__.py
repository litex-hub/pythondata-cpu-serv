import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post129"
version_tuple = (1, 0, 129)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post129")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post63"
data_version_tuple = (1, 0, 63)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post63")
except ImportError:
    pass
data_git_hash = "aa16bc40b6c7db767e05f460d8992721c7a8a55d"
data_git_describe = "v1.0-63-gaa16bc4"
data_git_msg = """\
commit aa16bc40b6c7db767e05f460d8992721c7a8a55d
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Wed Dec 2 15:55:45 2020 +0100

    Move ibus_cyc handling to serv_state

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
