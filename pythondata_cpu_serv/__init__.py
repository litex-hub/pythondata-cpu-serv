import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post78"
version_tuple = (1, 0, 78)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post78")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post25"
data_version_tuple = (1, 0, 25)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post25")
except ImportError:
    pass
data_git_hash = "acbedbe9c4bbff4bb0d2cdda725a95f2e1c42adc"
data_git_describe = "v1.0-25-gacbedbe"
data_git_msg = """\
commit acbedbe9c4bbff4bb0d2cdda725a95f2e1c42adc
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Tue May 26 22:52:09 2020 +0200

    Prepare for release

"""

# Tool version info
tool_version_str = "0.0.post53"
tool_version_tuple = (0, 0, 53)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post53")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
