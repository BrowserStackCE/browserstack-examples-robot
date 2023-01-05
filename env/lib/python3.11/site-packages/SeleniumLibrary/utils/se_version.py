import selenium
import re

def _version_to_tuple(version_string):
    version = [int(re.match(r'\d*', v).group() or 0) for v in version_string.split('.')]
    missing = [0] * (3 - len(version))
    return tuple(version + missing)[:3]

SE_VERSION = _version_to_tuple(selenium.__version__)
SE2 = SE_VERSION[0] == 2
SE3 = SE_VERSION[0] == 3
SE4 = SE_VERSION[0] == 4