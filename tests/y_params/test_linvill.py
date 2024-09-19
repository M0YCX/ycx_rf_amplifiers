from ycx_complex_numbers import Y, Z
from ycx_rf_amplifiers.y_params import calc_linvill_stability, calc_linvill_stability2


def test_good_inputs():
    yi = Y(14 + 1j)
    yo = Y(0.2 + 2j)
    yf = Y(-14 + 0.8j)
    yr = Y(0.2 - 0.2j)

    C = round(calc_linvill_stability(yi, yo, yf, yr), 2)
    assert C == 0.48

    C2 = round(calc_linvill_stability2(y11=yi, y12=yr, y21=yf, y22=yo), 2)
    assert C2 == 0.48

def test_bad_inputs():
    yi = Z(14 + 1j)
    yo = Z(0.2 + 2j)
    yf = Z(-14 + 0.8j)
    yr = Z(0.2 - 0.2j)

    try:
        calc_linvill_stability(yi, yo, yf, yr)
    except TypeError as e:
        print(e)
    else:
        assert False