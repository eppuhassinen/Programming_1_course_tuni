"""
COMP.CS.100 Programming 1
Yogi bear tehtävä
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def repeat_name(name, amount):
    """
    Prints the 4th 5th and 6th lines
    :param name: name to print
    :param amount: amount of times to print
    :return: none
    """
    for _ in range(0, amount):
        print(name + ",", name, "Bear")


def verse(current_verse, name):
    """
    Prints the verse to the screen with the name
    :param current_verse: The line of a verse
    :param name: current bear name
    :return: none
    """
    print(current_verse)
    print(name + ",", name)
    print(current_verse)
    repeat_name(name, 3)
    print(current_verse)
    repeat_name(name, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
