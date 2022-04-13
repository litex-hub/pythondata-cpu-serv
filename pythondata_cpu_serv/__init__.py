import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.1.0.post160"
version_tuple = (1, 1, 0, 160)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post160")
except ImportError:
    pass

# Data version info
data_version_str = "1.1.0.post34"
data_version_tuple = (1, 1, 0, 34)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post34")
except ImportError:
    pass
data_git_hash = "2df592340f43a4a2951362960909863812bb8c1f"
data_git_describe = "1.1.0-34-g2df5923"
data_git_msg = """\
commit 2df592340f43a4a2951362960909863812bb8c1f
Author: Usman <32096123+usmnzain@users.noreply.github.com>
Date:   Wed Apr 13 10:48:58 2022 +0500

    Compliance update
    
    Updated serv to support latest version of riscv-arch-test (v2.6.1)

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_serv."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_serv".format(f))
    return fn
