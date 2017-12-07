import os
from ctypes import cdll, POINTER, c_uint64, c_size_t, c_double


jsdlib = None


def rjsd(x, y):
    """
    :param x: yack.core.SparseArray
    :param y: yack.core.SparseArray
    :return: float
    """
    x.normalize()
    y.normalize()
    xcols_p = x.cols.ctypes.data_as(POINTER(c_uint64))
    xdata_p = x.data.ctypes.data_as(POINTER(c_double))
    ycols_p = y.cols.ctypes.data_as(POINTER(c_uint64))
    ydata_p = y.data.ctypes.data_as(POINTER(c_double))
    return jsdlib.jsd(xcols_p, xdata_p, len(x), ycols_p, ydata_p, len(y))


def _find_lib(directory, prefix):
    for name in os.listdir(directory):
        fullname = os.path.join(directory, name)
        if os.path.isfile(fullname) and name.startswith(prefix) \
                and name.endswith("so"):
            return fullname

    raise ValueError("Library '%s' not found" % prefix)


if __name__ == "__main__":
    raise RuntimeError()
else:
    libdir = os.path.dirname(os.path.abspath(__file__))
    jsdlib = cdll.LoadLibrary(_find_lib(libdir, "jsd"))
    jsdlib.jsd.argtypes = [POINTER(c_uint64), POINTER(c_double), c_size_t,
                           POINTER(c_uint64), POINTER(c_double), c_size_t]
    jsdlib.jsd.restype = c_double
