# Simultaneous Conjugate Match from S-Parameters

> Ref:
> * RF Circuit Design 2nd Edition by Chris Bowick [page 142]
> * https://www.youtube.com/watch?v=0LGObt5iJXY
> * https://www.youtube.com/watch?v=2AyLIF-g5LM

For uncondtionally stable transistors - tested using the Rollett Stability Factor.

Simultaneous Conjugate Match for maximum power transfer from Source to Load.

Find the *load reflection coefficient* for a conjugate match:

$$
C_2 = S_{22} - (D_S S_{11}^*)
$$

Where:
* $D_S$ is the intermediate result from the Rollett Stability Factor
* $S_{11}^*$ is the complex conjugate of $S_{11}$ (real/mag the same, but opposite -imag/-angle)

Next:

$$
B_2 = 1 + |S_{22}|^2 - |S_{11}|^2 - |D_S|^2
$$

The *magnitude* of the reflection coefficient:

$$
|\Gamma_L| = \frac{B_2 \pm \sqrt{B_2^2 - 4|C_2|^2}}{2|C_2|}
$$

where:
* $\pm$ is the opposite sign to $B_2$

The *angle* of the load reflection coefficient is simply the negative of the angle of $C_2$ (or negative of the imaginary if in complex form)

The load reflection coefficient can be plotted on a Smith Chart to find the corresponding load impedance. Or substitute $\Gamma_L$ in

$$
\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}
$$

and solve for $Z_L$:

$$
Z_L = Z_0 \bigg(\frac{1 + \Gamma}{1 - \Gamma}\bigg)
$$

With the load coefficient we can now calculate the source-reflection coefficient to properly terminate the transistor's input:

$$
\Gamma_S = \bigg[S_{11} + \frac{S_{12} S_{21} \Gamma_L}{1 - (\Gamma_L \cdot S_{22})}\bigg]^*
$$

Where
* $\bigg[ \ldots \bigg]^*$ indiates that you should take the conjugate of the quantity in brackets.

As with $\Gamma_L$ this can again be plotted on a Smith Chart or calculated as above to find $Z_S$

Finally we calculate the **Transducer Gain**:

$$
G_T = \frac{|S_{11}|^2 (1 - |\Gamma_S|^2) (1 - |\Gamma_L|^2)}{|(1 - S_{11}\Gamma_S) (1 - S_{22}\Gamma_L) - S_{12} S_{21} \Gamma_L \Gamma_S|^2}
$$

Also, in addtion we can calc the *Intrinsic Forward Gain* (i.e. if the transistor was input & output matched with 50 Ohms ($Z_0$)):

$$
IFG = \big|S_{21}\big|^2
$$