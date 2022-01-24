"""
Liukulukujen (desimaalilukujen) vertaileminen
Nimi: Eppu Hassinen
Opiskelijanumero: 50044786
"""


EPSILON: float = 0.00000001


def compare_floats(a, b, EPSILON):
    """
    Compares the floats and returns a boolean if they are close enoungh
    to each other
    :param a: float, first float
    :param b: float, second float
    :return: returns a boolean
    """

    if abs(a - b) < EPSILON:
        return True

    return False
