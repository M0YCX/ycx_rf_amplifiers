import math
from ycx_complex_numbers import Complex, Y

from ycx_rf_amplifiers.y_params import (
    calc_linvill_stability,
    y_max_available_gain_db,
)


def calc_simultaneous_conjugate_match(yi=None, yo=None, yf=None, yr=None):
    """Simultanueous Conjugate Match from Transistor Y-Paramters
    Transistor Y-parameters at a given frequency and bias conditions
    in mmhos:
        yi = input admittance
        yo = output admittance
        yf = forward-transfer admittance
        yr = reverse-transfer admittance
    """
    for p in (yi, yo, yf):
        if not isinstance(p, Y):
            raise TypeError(
                "All admittance inputs must be type Y Complex number instances"
            )

    gi = yi.real
    bi = yi.imag

    go = yo.real
    bo = yo.imag

    C = calc_linvill_stability(yi, yo, yf, yr)

    if C >= 1:
        raise ValueError("Failed Linvill Stability Test")

    mag_db = y_max_available_gain_db(yi, yo, yf)

    # Simultaneous Conjugate Match:-

    # Source:
    GS = math.sqrt((2 * gi * go - (yf * yr).real) ** 2 - abs(yf * yr) ** 2) / (2 * go)

    BS = (1j * -bi) + 1j * ((yf * yr).imag / (2 * go))

    YS = Y(GS + BS.imag * 1j)

    # Load:
    GL = (GS * go) / gi

    BL = (1j * -bo) + 1j * ((yf * yr).imag / (2 * gi))

    YL = Y(GL + BL.imag * 1j)

    tYL = complex(GL, -BL.imag)

    # Transducer Gain
    # fmt: off
    GT = (
        4 * GS * GL * abs(yf) ** 2
    ) / (
        abs((yi + YS) * (yo + YL) - yf * yr) ** 2
    )
    # fmt: on
    GT_db = 10 * math.log10(GT)
    return {
        "yi": yi,
        "yo": yo,
        "yf": yf,
        "yr": yr,
        "linvill_test": C,
        "transducer_gain_db": GT_db,
        "maximum_available_gain_db": mag_db,
        "YS": YS,
        "YL": YL,
    }
