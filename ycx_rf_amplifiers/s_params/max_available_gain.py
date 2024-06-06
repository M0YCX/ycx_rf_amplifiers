import math
from ycx_complex_numbers import Complex, S
from ycx_rf_amplifiers.s_params import (
    calc_rollett_stability,
    calc_determinant_of_S_matrix,
)


def s_max_available_gain_db(s11=None, s22=None, s21=None, s12=None):
    """
    Calculate the maximum available gain from S-Parameters

    Args:
        s11 (Complex): Forward Reflection coefficient of port 1
        s22 (Complex): Reverse Reflection coefficient of port 2
        s21 (Complex): Forward Transmission coefficient from port 1 to port 2
        s12 (Complex): Reverse Transmission coefficient from port 2 to port 1

    Returns:
        float: Maximum available gain in dB
    """
    for p in (s11, s22, s21, s12):
        if not isinstance(p, S):
            raise TypeError("All inputs must be type S Complex number instances")

    Ds = calc_determinant_of_S_matrix(s11, s22, s21, s12)

    K = calc_rollett_stability(s11, s22, s21, s12)
    if K > 1:
        pass
    else:
        raise ValueError("K must be greater than 1")

    B1 = 1 + abs(s11) ** 2 - abs(s22) ** 2 - abs(Ds) ** 2

    if B1 < 0:
        k_calc = K + math.sqrt(K**2 - 1)
    else:
        k_calc = K - math.sqrt(K**2 - 1)

    mag_db = 10 * math.log10(abs(s21) / abs(s12)) + 10 * math.log10(abs(k_calc))

    return mag_db
