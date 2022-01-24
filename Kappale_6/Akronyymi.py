"""
Akronyymi
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def create_an_acronym(name_input):
    """
    Creates an acronym from the input
    :param name_input: string, not empty
    :return: acronym
    """
    name_list = name_input.split()
    acronym = ""
    for word in name_list:
        acronym += word[0]
        
    return acronym.upper()


create_an_acronym("central intelligence agency")
