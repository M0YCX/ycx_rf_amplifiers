from ycx_complex_numbers import Complex, S

def calc_rollett_stability(s11=None, s22=None, s21=None, s12=None):
    """
    Calculate the Rollett stability factor for a biased transistor

    Args:
        s11 (Complex): Forward Reflection coefficient of port 1
        s22 (Complex): Reverse Reflection coefficient of port 2
        s21 (Complex): Forward Transmission coefficient from port 1 to port 2
        s12 (Complex): Reverse Transmission coefficient from port 2 to port 1

    Returns:
        float: The Rollett stability factor (K). K>1 is unconditionally stable.
    """
    for p in (s11, s22, s21, s12):
        if not isinstance(p, S):
            raise TypeError("All inputs must be type S Complex number instances")

    Ds = s11 * s22 - s12 * s21

    K = (1 + abs(Ds) ** 2 - abs(s11) ** 2 - abs(s22) ** 2) / (2 * abs(s21) * abs(s12))

    return K