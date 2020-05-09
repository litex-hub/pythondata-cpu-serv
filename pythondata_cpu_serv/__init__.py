import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post72"
version_tuple = (1, 0, 72)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post72")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post21"
data_version_tuple = (1, 0, 21)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post21")
except ImportError:
    pass
data_git_hash = "40b018af6667b54e5c4f05d4844148f4c04e09e7"
data_git_describe = "v1.0-21-g40b018a"
data_git_msg = """\
commit 40b018af6667b54e5c4f05d4844148f4c04e09e7
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Fri May 8 22:56:31 2020 +0200

    Align RISC-V compliance test target code with upstream changes

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
