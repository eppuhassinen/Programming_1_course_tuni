"""
Kolmion kulmien summa
Nimi: Eppu Hassinen
Opiskelijanumero: 50044786
"""


def calculate_angle(angle_1, angle_2=90):
    """
    Calculates the third angle of a triangle, if input has only one angle, the
    funktion uses 90 degrees as the second angle
    :param angle_1: float, first angle
    :param angle_2: float, second angle
    :return: the third angle
    """

    third_angle = 180 - angle_1 - angle_2
    return third_angle
