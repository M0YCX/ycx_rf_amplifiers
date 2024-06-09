# Simultaneous Conjugate Match from Y-Parameters

> Ref: RF Circuit Design 2nd Edition by Chris Bowick

(for uncondtionally stable transistors)

Simultaneous Conjugate Match for maximum power transfer from Source to Load:

Source:
$$
G_S = \frac{\sqrt{[2 g_i g_o - Re(y_f y_r)]^2 - |y_f y_r|^2}}{2 g_o}
$$

$$
B_S = -jb_i + \frac{Im(y_f y_r)}{2 g_o}
$$

Load:
$$
G_L = \frac{\sqrt{[2 g_i g_o - Re(y_f y_r)]^2 - |y_f y_r|^2}}{2 g_i} = \frac{G_S g_o}{g_i}
$$

$$
B_L = -jb_o + \frac{Im(y_f y_r)}{2 g_i}
$$

where:
* $y*$ values are in mmhos.
* $y_f$ is the forward-transfer admittance
* $y_r$ is the reverse-transfer admittance
* $g_i, g_o$ are the input and output conductances respectively (real parts of $y_i, y_o$)
* $b_i, b_o$ are the input and output susceptances respectively (imaginary parts of $y_i, y_o$)
* $G_S$ is the source conductance
* $B_S$ is the source susceptance
* $G_L$ is the load conductance
* $B_L$ is the load susceptance
* $Re$ is the real part of the $(...)$
* $Im$ is the imaginary part of the $(...)$

## Transducer Gain

$$
G_T = \frac{4 G_S G_L | y_f|^2}{|(y_i + Y_S) (y_o +Y_L) - y_f y_r |^2}
$$