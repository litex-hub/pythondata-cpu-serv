import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post140"
version_tuple = (1, 1, 0, 140)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post140")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post23"
data_version_tuple = (1, 1, 0, 23)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post23")
except ImportError:
    pass
data_git_hash = "07193819972aed16e8474913dbbbee5e01570e58"
data_git_describe = "1.1.0-23-g0719381"
data_git_msg = """\
commit 07193819972aed16e8474913dbbbee5e01570e58
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Sat Jan 1 17:15:00 2022 +0100

    Add ViDBo support

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
