"""
COMP.CS.100 Programming 1
Print a box with input error checking
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def print_box(width, height, mark):
    """
    Prints a box
    :param width: the width of the box
    :param height: the height of the box
    :param mark: mark to use
    :return:
    """

    for _ in range(0, height):
        print(mark * width)


def read_input(text):
    """
    asks for a number, if it's equal or less than 0, then ask again
    :param text: text to print
    :return: number thats bigger than 0
    """
    on = True

    while on:
        n = int(input(text))
        if n > 0:
            return n


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)


if __name__ == "__main__":
    main()
