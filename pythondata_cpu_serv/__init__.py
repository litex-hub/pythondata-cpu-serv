import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post69"
version_tuple = (1, 0, 69)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post69")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post18"
data_version_tuple = (1, 0, 18)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post18")
except ImportError:
    pass
data_git_hash = "95c5c027a1bb52054df4daa8f3fa3106e0294b33"
data_git_describe = "v1.0-18-g95c5c02"
data_git_msg = """\
commit 95c5c027a1bb52054df4daa8f3fa3106e0294b33
Author: Gwenhael Goavec-Merou <gwenhael.goavec-merou@trabucayre.com>
Date:   Wed May 6 20:10:13 2020 +0200

    Add Saanlima pipistrello spartan6 LX45

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
