import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post260"
version_tuple = (1, 0, 260)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post260")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post148"
data_version_tuple = (1, 0, 148)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post148")
except ImportError:
    pass
data_git_hash = "99f82af6eb6b7fe5dad682bd315349fcd37fa102"
data_git_describe = "v1.0-148-g99f82af"
data_git_msg = """\
commit 99f82af6eb6b7fe5dad682bd315349fcd37fa102
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Sun Oct 3 23:28:45 2021 +0200

    Simplify optional MDU logic

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
