from ycx_complex_numbers import Complex, Y

def y_max_available_gain(yi=None, yo=None, yf=None):
    for p in (yi, yo, yf):
        if not isinstance(p, Y):
            raise TypeError("All admittance inputs must be type Y Complex number instances")

    gi = yi.real
    go = yo.real

    mag = (abs(yf) ** 2) / (4 * gi * go)

    return mag
