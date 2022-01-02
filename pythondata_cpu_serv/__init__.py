import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post143"
version_tuple = (1, 1, 0, 143)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post143")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post26"
data_version_tuple = (1, 1, 0, 26)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post26")
except ImportError:
    pass
data_git_hash = "aa8550b937f7d77f71011a985d23c9d154fd4588"
data_git_describe = "1.1.0-26-gaa8550b"
data_git_msg = """\
commit aa8550b937f7d77f71011a985d23c9d154fd4588
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Sun Jan 2 21:58:32 2022 +0100

    Remove doc for removed modules

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
