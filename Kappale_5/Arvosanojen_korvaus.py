"""
Arvosanojen korvaus
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def convert_grades(grades):
    """
    Converts all values wich are not 0 to 6
    :param grades: list, list of grades [0,5]
    :return: None
    """

    for i in range(len(grades)):
        if grades[i] != 0:
            grades[i] = 6
