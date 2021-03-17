import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post194"
version_tuple = (1, 0, 194)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post194")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post99"
data_version_tuple = (1, 0, 99)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post99")
except ImportError:
    pass
data_git_hash = "9b84539bc0a72fb4c99a15cd894ffb62e3cc8e05"
data_git_describe = "v1.0-99-g9b84539"
data_git_msg = """\
commit 9b84539bc0a72fb4c99a15cd894ffb62e3cc8e05
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Wed Mar 17 21:14:41 2021 +0100

    Add LibreCores badge

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
