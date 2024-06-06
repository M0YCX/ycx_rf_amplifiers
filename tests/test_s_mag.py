from ycx_complex_numbers import S, Z
from ycx_rf_amplifiers.s_params import s_max_available_gain_db


def test_good_inputs():
    s11 = S().from_polar(0.4, 162)
    s22 = S().from_polar(0.35, -39)
    s21 = S().from_polar(5.2, 63)
    s12 = S().from_polar(0.04, 60)

    mag_db = round(s_max_available_gain_db(s11, s22, s21, s12), 1)
    assert mag_db == 16.1


def test_bad_inputs():
    s11 = Z().from_polar(0.4, 162)
    s22 = Z().from_polar(0.35, -39)
    s21 = Z().from_polar(5.2, 63)
    s12 = Z().from_polar(0.04, 60)

    try:
        s_max_available_gain_db(s11, s22, s21, s12)
    except TypeError as e:
        print(e)
    else:
        assert False
