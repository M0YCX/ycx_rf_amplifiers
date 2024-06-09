from ycx_complex_numbers import Y, Z
from ycx_rf_amplifiers.y_params import calc_simultaneous_conjugate_match


def test_good_inputs():
    # input admittance:
    yi = Y(8 + 5.7j)
    # output admittance:
    yo = Y(0.4 + 1.5j)
    # forward-transfer admittance:
    yf = Y(52 - 20j)
    # reverse-transfer admittance:
    yr = Y(0.01 - 0.1j)

    cj = calc_simultaneous_conjugate_match(yi, yo, yf, yr)
    print(cj)
    assert round(cj["linvill_test"], 4) == 0.7106
    assert round(cj["maximum_available_gain_db"], 1) == 23.8
    assert round(cj["transducer_gain_db"], 1) == 23.6
    assert round(cj["YS"].real, 3) == 6.931
    assert round(cj["YS"].imag, 3) == -12.45
    assert round(cj["YL"].real, 3) == 0.347
    assert round(cj["YL"].imag, 3) == -1.837


def test_bad_inputs():
    yi = Z().from_polar(0.4, 162)
    yo = Z().from_polar(0.35, -39)
    yf = Z().from_polar(5.2, 63)
    yr = Z().from_polar(0.04, 60)

    try:
        calc_simultaneous_conjugate_match(yi, yo, yf, yr)
    except TypeError as e:
        print(e)
    else:
        assert False
