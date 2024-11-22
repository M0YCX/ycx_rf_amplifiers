from ycx_complex_numbers import NetY
from ycx_rf_amplifiers.models import HybridPi
import pytest


class TestHybridPi:
    @pytest.fixture
    def t1(self):
        return {
            "B0": 100.0,
            "Rbp": 10.0,
            "Ccb": 5.0 * 10**-12,
            "Ie": 10.0 * 10**3,
            "Re": 6.8,
            "Le": 10.0 * 10**-9,
            "FT": 300.0 * 10**6,
        }

    def test_hybrid_pi(self, t1):
        print(f"t1={t1}")

        hpi = HybridPi(**t1)
        print(f"hpi={hpi}")

        y = hpi.calc(F=10.00 * 10**6)
        print(f"y={y}")

        yexpected = NetY(
            y11=0.00151 + 0.00359j,
            y12=-0.00001 - 0.00031j,
            y21=0.10256 - 0.01436j,
            y22=0.00005 + 0.00064j,
        )
        assert y.equals(yexpected, precision=5)
