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
            "FT": 300.0 * 10**6,
        }

    def test_hybrid_pi(self, t1):
        hpi = HybridPi(**t1)
        y = hpi.calc(F=10.00 * 10**6)

        yexpected = NetY(
            y11=0.00549 + 0.01167j,
            y12=-0.00004 - 0.00030j,
            y21=0.35800 - 0.05655j,
            y22=0.00018 + 0.00144j,
        )
        assert y.equals(yexpected, precision=5)
