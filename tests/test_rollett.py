from ycx_complex_numbers import S, Z
from ycx_rf_amplifiers.s_params import calc_rollett_stability


def test_good_inputs():
    s11 = S().from_polar(0.4, 162)
    s22 = S().from_polar(0.35, -39)
    s12 = S().from_polar(0.04, 60)
    s21 = S().from_polar(5.2, 63)

    K = calc_rollett_stability(s11, s22, s12, s21)
    assert round(K, 3) == 1.736


def test_bad_inputs():
    s11 = Z().from_polar(0.4, 162)
    s22 = Z().from_polar(0.35, -39)
    s12 = Z().from_polar(0.04, 60)
    s21 = Z().from_polar(5.2, 63)

    try:
        calc_rollett_stability(s11, s22, s12, s21)
    except TypeError as e:
        print(e)
    else:
        assert False
