import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post155"
version_tuple = (1, 1, 0, 155)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post155")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post31"
data_version_tuple = (1, 1, 0, 31)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post31")
except ImportError:
    pass
data_git_hash = "b74344bb480a391e2642f4a1383015ded4133c85"
data_git_describe = "1.1.0-31-gb74344b"
data_git_msg = """\
commit b74344bb480a391e2642f4a1383015ded4133c85
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Thu Jan 20 23:46:48 2022 +0100

    Store GDS file as artifact after OpenLANE build

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
