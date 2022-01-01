import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post141"
version_tuple = (1, 1, 0, 141)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post141")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post24"
data_version_tuple = (1, 1, 0, 24)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post24")
except ImportError:
    pass
data_git_hash = "f04a510393585f0a68280c912ae568b2dccc11cf"
data_git_describe = "1.1.0-24-gf04a510"
data_git_msg = """\
commit f04a510393585f0a68280c912ae568b2dccc11cf
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Sat Jan 1 22:43:43 2022 +0100

    Remove unused parameter from serv_mem_if

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
