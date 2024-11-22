import math

from ycx_complex_numbers import Complex, Neta, NetY, Y, Z

class HybridPi(object):
    """Generate a common-emitter Y parameters from the hybrid-pi model"""
    def __init__(self, B0=None, Rbp=10.0, Ccb=None, Ie=None, Re=0, Le=0, FT=None):
        self.B0 = B0
        self.Rbp = Rbp
        self.Ccb = Ccb
        self.Ie = Ie
        self.Re = Re
        self.Le = Le
        self.re = 26 / (Ie * 10**-3) # mA
        self.FT = FT

    def calc(self, F=None):
        self.F = F
        w = 2 * math.pi * F
        jw = 1j * w

        beta = Complex(self.B0 / (1 + (1j * self.B0 * F) / self.FT))

        Ze = Z(self.re + self.Re + 1j * (w * self.Le))

        # base spreading resistor as ABCD matrix for cascading below
        Rbp_A = Neta(a11=1, a12=self.Rbp, a21=0, a22=1)

        y11e = Y(1 / (Ze * (beta + 1)) + (jw * self.Ccb))
        y12e = Y(0 - (jw * self.Ccb))
        y21e = Y(beta / (Ze * (beta + 1)) - (jw * self.Ccb))
        y22e = Y(0 + (jw * self.Ccb))
        ye = NetY(y11=y11e, y12=y12e, y21=y21e, y22=y22e)

        # Cascade the base spreading resistance to the hybrid-pi amplifier
        Ae = ye.to_a()
        self.Ye = (Rbp_A @ Ae).to_Y()

        return self.Ye
