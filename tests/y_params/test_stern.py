from ycx_complex_numbers import Y, Z
from ycx_rf_amplifiers.y_params import calc_stern_stability


def test_good_inputs():
    yi = Y(14 + 1j)
    yo = Y(0.2 + 2j)
    yf = Y(-14 + 0.8j)
    yr = Y(0.2 - 0.2j)

    K = round(calc_stern_stability(yi, yo, yf, yr, 50, 50), 0)
    assert K == 4845


def test_bad_inputs():
    yi = Z(14 + 1j)
    yo = Z(0.2 + 2j)
    yf = Z(-14 + 0.8j)
    yr = Z(0.2 - 0.2j)

    try:
        calc_stern_stability(yi, yo, yf, yr, 50, 50)
    except TypeError as e:
        print(e)
    else:
        assert False
