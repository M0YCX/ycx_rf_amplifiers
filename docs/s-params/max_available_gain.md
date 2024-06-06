# Maximum Available Gain (MAG) from S-Parameters

> Ref:
> * RF Circuit Design 2nd Edition by Chris Bowick [page 142]
> * https://www.youtube.com/watch?v=0LGObt5iJXY

Calc intermediate $B_1$:
$$
B_1 = 1 + |S_{11}|^2 - |S_{22}|^2 - |D_S|^2
$$

where $D_S$ is from the Rollett Stability Factor.

MAG is calculated:
$$
MAG = 10 log\frac{|S_{21}|}{|S_{12}|} + 10 log \big| K \pm \sqrt{K^2 - 1}\big|
$$

$MAG$ is returned in $dB$

$\pm$ is
* if $B_1$ is negative, use $+$
* if $B_1$ is positive, use $-$

## Maximum Stable Gain (MSG)

$$
G_T < 10 log \bigg|\frac{S_{21}}{S_{12}}\bigg|
$$