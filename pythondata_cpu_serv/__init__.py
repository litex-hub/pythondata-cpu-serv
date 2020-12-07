import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post135"
version_tuple = (1, 0, 135)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post135")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post69"
data_version_tuple = (1, 0, 69)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post69")
except ImportError:
    pass
data_git_hash = "731ca8bb45f9182cd6d0ababcad3055a305fe298"
data_git_describe = "v1.0-69-g731ca8b"
data_git_msg = """\
commit 731ca8bb45f9182cd6d0ababcad3055a305fe298
Author: Bruno Flores <bruno@brunoflores.com.br>
Date:   Sat Oct 24 12:04:41 2020 +0000

    Allow for a configurable toolchain prefix.

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
