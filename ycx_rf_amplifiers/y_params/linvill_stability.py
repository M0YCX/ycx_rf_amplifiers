from ycx_complex_numbers import Complex, Y

def calc_linvill_stability(yi=None, yo=None, yf=None, yr=None):
    """
    Calculate the stability factor for an RF Amplifier

    Args:
        yi (Complex): Input Admittance
        yo (Complex): Output Admittance
        yf (Complex): Forward-Transfer Admittance
        yr (Complex): Reverse-Transfer Admittance

    Returns:
        float: The stability factor.
    """
    for p in (yi, yo, yf, yr):
        if not isinstance(p, Y):
            raise TypeError("All inputs must be type Y Complex number instances")

    C = abs(yf.c * yr.c) / (2 * yi.real * yo.real - (yf.c * yr.c).real)

    return C