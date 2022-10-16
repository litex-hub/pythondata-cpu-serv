import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.2.0.post146"
version_tuple = (1, 2, 0, 146)
try:
    from packaging.version import Version as V
    pversion = V("1.2.0.post146")
except ImportError:
    pass

# Data version info
data_version_str = "1.2.0.post4"
data_version_tuple = (1, 2, 0, 4)
try:
    from packaging.version import Version as V
    pdata_version = V("1.2.0.post4")
except ImportError:
    pass
data_git_hash = "7c004e8f7b0776cf4664a5311625f534eaff49f1"
data_git_describe = "1.2.0-4-g7c004e8"
data_git_msg = """\
commit 7c004e8f7b0776cf4664a5311625f534eaff49f1
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Sun Oct 16 20:04:56 2022 +0200

    Add reset input for Arty A7 target

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
