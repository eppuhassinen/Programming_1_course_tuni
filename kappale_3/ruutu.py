"""
COMP.CS.100 Programming 1
Tehtävä: ruutu
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


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
