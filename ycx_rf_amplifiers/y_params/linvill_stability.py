from ycx_complex_numbers import Complex, Y

def calc_linvill_stability(yi=None, yo=None, yf=None, yr=None):
    """
    Calculate the Linvill stability factor for a biased transistor

    Args:
        yi (Complex): Input Admittance
        yo (Complex): Output Admittance
        yf (Complex): Forward-Transfer Admittance
        yr (Complex): Reverse-Transfer Admittance

    Returns:
        float: The stability factor (C). C<1 is stable.
    """
    for p in (yi, yo, yf, yr):
        if not isinstance(p, Y):
            raise TypeError("All inputs must be type Y Complex number instances")

    C = abs(yf.c * yr.c) / (2 * yi.real * yo.real - (yf.c * yr.c).real)

    return C

def calc_linvill_stability2(y11=None, y12=None, y21=None, y22=None):
    return calc_linvill_stability(yi=y11, yr=y12, yf=y21, yo=y22)