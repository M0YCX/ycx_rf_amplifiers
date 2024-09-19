from ycx_complex_numbers import Complex, Y

def calc_stern_stability(yi=None, yo=None, yf=None, yr=None, GS=None, GL=None):
    """
    Calculate the Stern stability factor for an RF Amplifier

    Args:
        yi (Complex): Input Admittance
        yo (Complex): Output Admittance
        yf (Complex): Forward-Transfer Admittance
        yr (Complex): Reverse-Transfer Admittance
        GS (float): Conductance of the Source
        GL (float): Conductance of the Load

    Returns:
        float: The Stern (K) stability factor. K>1 is stable.
    """
    for p in (yi, yo, yf, yr):
        if not isinstance(p, Y):
            raise TypeError("All admittance inputs must be type Y Complex number instances")

    gi = yi.real
    go = yo.real

    K = (2 * (gi + GS) * (go + GL)) / (abs(yr.c * yf.c) + (yr.c * yf.c).real)

    return K

def calc_stern_stability2(y11=None, y12=None, y21=None, y22=None, GS=None, GL=None):
    return calc_stern_stability(yi=y11, yr=y12, yf=y21, yo=y22, GS=GS, GL=GL)