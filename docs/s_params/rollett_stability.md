# The Rollett Stability Factor from S-Parameters

> Ref: RF Circuit Design 2nd Edition by Chris Bowick

Calc intermediate quantity $D_S$:

$$
D_S = S_{11} S_{22} - S_{12} S_{21}
$$

The Rollett Stability Factor (K) is then calculated:

$$
K = \frac{1 + |D_S|^2 - |S_{11}|^2 - |S_{22}|^2}{2 \cdot |S_{21}| \cdot |S_{12}|}
$$

If $K > 1$ the transistor is unconditionally stable for any combination of source and load impedance.
