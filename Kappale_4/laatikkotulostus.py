"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
Nimi: Eppu Hassinen
Opiskelijanumero: 50044786
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    Prints a box
    :param width: int
    :param height: int
    :param border_mark: string, default "#"
    :param inner_mark: string, default " "
    :return:
    """

    # prints the top row
    print(border_mark * width)

    # "i" is the current row printing
    i = 2
    while i <= height - 1:
        print(border_mark, inner_mark * (width - 2), border_mark, sep="")
        i += 1

    # final row
    print(border_mark * width)


def main():
    print_box(5, 4)
    print()
    print_box(3, 8, "*")
    print()
    print_box(5, 4, "O", "o")
    print()
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
