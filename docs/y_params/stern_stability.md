# Stern Stability Factor from Y-Parameters

> Ref: RF Circuit Design 2nd Edition by Chris Bowick

$$
K = \frac{2(g_i + G_S)(g_o + G_L)}{|y_r y_f| + Re(y_r y_f)}
$$

* $|\ \ |$ is the magnitude if the complex product in brackets
* $y_r$ is the reverse-transfer admittance
* $y_f$ is the forward-transfer admittance
* $g_i$ is the input conductance
* $g_o$ is the output conductance
* $Re()$ is the real part of the complex product in parenthesis
* $G_S$ is the source conductance
* $G_L$ is the load conductance

If $K > 1$ the circuit will be stable for the given source and load conductances.