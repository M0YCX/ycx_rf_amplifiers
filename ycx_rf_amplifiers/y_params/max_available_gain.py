import math
from ycx_complex_numbers import Complex, Y

def y_max_available_gain(yi=None, yo=None, yf=None):
    """
     Calculate the Maximum Available Gain for an RF Amplifier

    Args:
        yi (Complex): Input Admittance
        yo (Complex): Output Admittance
        yf (Complex): Forward-Transfer Admittance

    Returns:
        float: The Maximum Available Gain.
    """
    for p in (yi, yo, yf):
        if not isinstance(p, Y):
            raise TypeError("All admittance inputs must be type Y Complex number instances")

    gi = yi.real
    go = yo.real

    mag = (abs(yf) ** 2) / (4 * gi * go)

    return mag

def y_max_available_gain_db(yi=None, yo=None, yf=None):
    """
     Calculate the Maximum Available Gain in Decibels for an RF Amplifier

    Args:
        yi (Complex): Input Admittance
        yo (Complex): Output Admittance
        yf (Complex): Forward-Transfer Admittance

    Returns:
        float: The Maximum Available Gain in Decibels.
    """
    return 10 * math.log10(y_max_available_gain(yi=yi, yo=yo, yf=yf))