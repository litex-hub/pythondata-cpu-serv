import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post184"
version_tuple = (1, 0, 184)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post184")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post95"
data_version_tuple = (1, 0, 95)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post95")
except ImportError:
    pass
data_git_hash = "a6292d46a2030bb56ada7637bc4d56131e94c4f4"
data_git_describe = "v1.0-95-ga6292d4"
data_git_msg = """\
commit a6292d46a2030bb56ada7637bc4d56131e94c4f4
Author: somhi <jordisx@gmail.com>
Date:   Sun Feb 7 12:04:23 2021 +0100

    Add support for DECA Max 10 board

"""

# Tool version info
tool_version_str = "0.0.post89"
tool_version_tuple = (0, 0, 89)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post89")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
