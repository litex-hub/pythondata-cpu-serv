import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post67"
version_tuple = (1, 0, 67)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post67")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post16"
data_version_tuple = (1, 0, 16)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post16")
except ImportError:
    pass
data_git_hash = "c0fc72b3535c6525ad93653d327080d9c85e9a8e"
data_git_describe = "v1.0-16-gc0fc72b"
data_git_msg = """\
commit c0fc72b3535c6525ad93653d327080d9c85e9a8e
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Mon Apr 27 13:58:32 2020 +0200

    Add upduino2 servant target

"""

# Tool version info
tool_version_str = "0.0.post51"
tool_version_tuple = (0, 0, 51)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post51")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
