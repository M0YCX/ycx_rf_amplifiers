from ycx_complex_numbers import S

def calc_determinant_of_S_matrix(s11=None, s22=None, s21=None, s12=None):
    """
    Calculate the determinant of the S-matrix

    Args:
        s11 (Complex): Forward Reflection coefficient of port 1
        s22 (Complex): Reverse Reflection coefficient of port 2
        s21 (Complex): Forward Transmission coefficient from port 1 to port 2
        s12 (Complex): Reverse Transmission coefficient from port 2 to port 1

    Returns:
        float: Determinant of the S-matrix
    """
    for p in (s11, s22, s21, s12):
        if not isinstance(p, S):
            raise TypeError("All inputs must be type S Complex number instances")

    Ds = (s11 * s22) - (s12 * s21)

    return Ds