import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post151"
version_tuple = (1, 1, 0, 151)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post151")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post29"
data_version_tuple = (1, 1, 0, 29)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post29")
except ImportError:
    pass
data_git_hash = "7624365325d037cffad613cb9435818c55c5ea2f"
data_git_describe = "1.1.0-29-g7624365"
data_git_msg = """\
commit 7624365325d037cffad613cb9435818c55c5ea2f
Author: somhi <somhi@users.noreply.github.com>
Date:   Tue Jan 11 22:54:45 2022 +0100

    chameleon96 board support added (#74)
    
    * chameleon96 board added

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
