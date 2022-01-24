"""
Funktio listan alkioiden yhtäsuuruusvertailuun
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def are_all_members_same(members_to_check=[]):
    """
    Checks if the members of a list are all the same
    :param members_to_check: list of members to check
    :return: boolean
    """
    length = len(members_to_check)

    if length == 0:
        return True

    # checks if the list has same members for the amount of its length
    if members_to_check.count(members_to_check[0]) == length:
        return True

    # returns False if none of the tests have returned True
    return False
