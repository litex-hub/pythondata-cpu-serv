import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/olofk/serv"

# Module version
version_str = "1.0.post182"
version_tuple = (1, 0, 182)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post182")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post93"
data_version_tuple = (1, 0, 93)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post93")
except ImportError:
    pass
data_git_hash = "9a0b0e877c809629ced825a91cf4eed578c15eed"
data_git_describe = "v1.0-93-g9a0b0e8"
data_git_msg = """\
commit 9a0b0e877c809629ced825a91cf4eed578c15eed
Author: Olof Kindgren <olof.kindgren@gmail.com>
Date:   Thu Feb 4 15:15:26 2021 +0100

    Move shifter to mem_if
    
    This allows reusing the data bus registers for shift amount

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
