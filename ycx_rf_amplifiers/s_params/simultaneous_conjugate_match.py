import math
import numpy as np

from ycx_complex_numbers import Complex, S
from ycx_rf_amplifiers.s_params import (
    calc_determinant_of_S_matrix,
    calc_rollett_stability,
    s_max_available_gain_db,
)


def calc_simultaneous_conjugate_match(s11=None, s22=None, s21=None, s12=None):
    """Simultanueous Conjugate Match from Transistor S-Paramters."""

    for p in (s11, s22, s21, s12):
        if not isinstance(p, S):
            raise TypeError("All inputs must be type S Complex number instances")

    Ds = calc_determinant_of_S_matrix(s11, s22, s21, s12)
    K = calc_rollett_stability(s11, s22, s21, s12)

    if K <= 1:
        raise ValueError("K must be greater than 1")

    MAG_db = s_max_available_gain_db(s11, s22, s21, s12)

    cof_s11 = s11.conjugate
    C2 = s22 - (Ds * cof_s11)

    B2 = 1 + abs(s22) ** 2 - abs(s11) ** 2 - abs(Ds) ** 2
    if B2 < 0:
        b_calc = B2 + math.sqrt(B2**2 - 4 * abs(C2) ** 2)
    else:
        b_calc = B2 - math.sqrt(B2**2 - 4 * abs(C2) ** 2)
    maggammaL = b_calc / (2 * abs(C2))
    gammaL = Complex().from_polar(maggammaL, -C2.as_polar()["angle"])

    gammaS_conjugate = s11 + (s12 * s21 * gammaL) / Complex(1 - (gammaL * s22).c)
    gammaS = gammaS_conjugate.conjugate

    # fmt: off
    GT = (
        (
            abs(s21) ** 2
            * (1 - abs(gammaS) ** 2)
            * (1 - abs(gammaL) ** 2)
        ) / (
            abs(
                Complex(1 - s11.c * gammaS.c)
                * Complex(1 - s22.c * gammaL.c)
                - s12 * s21 * gammaL * gammaS
            )
            ** 2
        )
    )
    # fmt: on
    GT_db = 10 * math.log10(GT)

    IFG_db = 10 * math.log10(abs(s21) ** 2)

    return {
        "s11": s11,
        "s22": s22,
        "s21": s21,
        "s12": s12,
        "Ds": Ds,
        "K": K,
        "transducer_gain_db": GT_db,
        "intrinsic_forward_gain_db": IFG_db,
        "maximum_available_gain_db": MAG_db,
        "gammaS": gammaS,
        "gammaL": gammaL,
    }
