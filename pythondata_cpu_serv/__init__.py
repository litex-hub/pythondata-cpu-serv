import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post188"
version_tuple = (1, 1, 0, 188)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post188")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post46"
data_version_tuple = (1, 1, 0, 46)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post46")
except ImportError:
    pass
data_git_hash = "efe8ba832a9ad29bc85bd1ea8e3050160c3499e5"
data_git_describe = "1.1.0-46-gefe8ba8"
data_git_msg = """\
commit efe8ba832a9ad29bc85bd1ea8e3050160c3499e5
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Mon Jul 25 23:24:29 2022 +0200

    Set up Github CI testing matrix for compliance tests

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
