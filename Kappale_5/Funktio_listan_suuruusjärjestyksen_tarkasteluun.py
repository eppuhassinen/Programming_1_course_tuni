"""
Funktio listan suuruusjärjestyksen tarkasteluun
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def is_the_list_in_order(lst=[]):
    """
    Returns a boolean if the list is in order
    :param lst: list to check
    :return: Boolean
    """

    return lst == sorted(lst)


def main():
    print(is_the_list_in_order([1, 100, 100]))


if __name__ == '__main__':
    main()
