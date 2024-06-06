from ycx_complex_numbers import Y, Z
from ycx_rf_amplifiers.y_params import y_max_available_gain, y_max_available_gain_db


def test_good_inputs():
    yi = Y(14 + 1j)
    yo = Y(0.2 + 2j)
    yf = Y(-14 + 0.8j)

    mag = round(y_max_available_gain(yi, yo, yf), 2)
    assert mag == 17.56

def test_bad_inputs():
    yi = Z(14 + 1j)
    yo = Z(0.2 + 2j)
    yf = Z(-14 + 0.8j)

    try:
        y_max_available_gain(yi, yo, yf)
    except TypeError as e:
        print(e)
    else:
        assert False

def test_mag_db():
    yi = Y(14 + 1j)
    yo = Y(0.2 + 2j)
    yf = Y(-14 + 0.8j)

    mag_db = round(y_max_available_gain_db(yi, yo, yf), 2)
    assert mag_db == 12.44