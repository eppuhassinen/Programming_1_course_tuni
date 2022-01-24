"""
Nimien kääntö oikein päin
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def reverse_name(name_input):
    """
    Returns corrected name
    :param name_input: string, name
    :return: string, corrected name
    """
    comma_index = name_input.find(",")
    if comma_index == -1:
        return name_input

    name_list = name_input.split(",")
    return_list = []

    for i in range(1, len(name_list) + 1):
        name_list[-i] = name_list[-i].strip()
        if name_list[-i] != "":
            return_list.append(name_list[-i])

    name_list.reverse()
    return " ".join(return_list)
