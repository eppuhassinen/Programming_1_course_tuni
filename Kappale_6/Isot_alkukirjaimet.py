"""
Isot alkukirjaimet paikoilleen
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def capitalize_initial_letters(input_string):
    """
    Capitalizes first letter of each word
    :param input_string: string, words
    :return: string, fixed text
    """

    # returns empty string if input is empty string
    if len(input_string) == 0:
        return ""

    # input converted to a list
    string_list = input_string.split(" ")
    # string to store the fixed text
    fixed_string = ""

    # makes first letter of each word capitalized
    # makes everything else lowercase
    for word in string_list:
        fixed_string += " " + word[0].upper() + word[1:len(word)].lower()

    return fixed_string.lstrip()
