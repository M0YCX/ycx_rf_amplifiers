from ycx_complex_numbers import S, Z
from ycx_rf_amplifiers.s_params import calc_simultaneous_conjugate_match


def test_good_inputs():
    s11 = S().from_polar(0.4, 162)
    s22 = S().from_polar(0.35, -39)
    s21 = S().from_polar(5.2, 63)
    s12 = S().from_polar(0.04, 60)

    cj = calc_simultaneous_conjugate_match(s11, s22, s21, s12)
    print(cj)
    assert round(cj["K"], 3) == 1.736
    assert round(cj["transducer_gain_db"], 1) == 16.1
    assert round(cj["intrinsic_forward_gain_db"], 1) == 14.3
    assert round(cj["maximum_available_gain_db"], 1) == 16.1
    assert round(cj["gammaS"].real, 3) == -0.497
    assert round(cj["gammaS"].imag, 3) == -0.161
    assert round(cj["gammaL"].real, 3) == 0.379
    assert round(cj["gammaL"].imag, 3) == 0.307


def test_bad_inputs():
    s11 = Z().from_polar(0.4, 162)
    s22 = Z().from_polar(0.35, -39)
    s21 = Z().from_polar(5.2, 63)
    s12 = Z().from_polar(0.04, 60)

    try:
        calc_simultaneous_conjugate_match(s11, s22, s21, s12)
    except TypeError as e:
        print(e)
    else:
        assert False
