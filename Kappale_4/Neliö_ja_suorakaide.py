"""
Neliö ja suorakaide
Nimi: Eppu Hassinen
Opiskelijanumero: 50044786
"""
import math


def square(side_1):
    """
    Calculates the circumference and area of a square
    :param side_1: float, side 1 length
    :return: float, circumference; float, area
    """
    circum = side_1 * 4
    area = side_1 * side_1

    return circum, area


def rectangle(side_1, side_2):
    """
    Calculates the circumference and area of a rectangle
    :param side_1: float, side 1 length
    :param side_2: float, side 2 length
    :return: float, circumference; float, area
    """
    circum = side_1 * 2 + side_2 * 2
    area = side_1 * side_2

    return circum, area


def circle(radius):
    """
    Calculates the circumference and area of a circle
    :param radius: float, radius
    :return: float, circumference; float, area
    """
    circum = 2 * radius * math.pi
    area = math.pi * pow(radius, 2)

    return circum, area


def ask_for_lengths(sentence, amount_of_lengths):
    """
    Asks for the lengths with the sentences given and returns correct lengths
    :param sentence: string, sentence printed when asking for a length
    :param amount_of_lengths: int, amount of lengths returned
    :return: list, returns a list with the lengths
    """
    lengths = [0]
    lengths = lengths * amount_of_lengths
    i = 1
    while i <= amount_of_lengths:
        if amount_of_lengths == 1:
            lengths[i - 1] = float(input(f"{sentence}: "))
        else:
            lengths[i - 1] = float(input(f"{sentence} {i}: "))

        if lengths[i - 1] > 0:
            i += 1

    return lengths


def check_for_cmd(command):
    """
    check the command: s:square, r:rectangle, c:circle
    :param command: string, command
    :return: float, circum; float, area
    """

    if command == "s":
        lengths = ask_for_lengths(
            "Enter the length of the square's side", 1)
        circum, area = square(lengths[0])

    elif command == "r":
        lengths = ask_for_lengths(
            "Enter the length of the rectangle's side", 2)
        circum, area = rectangle(lengths[0], lengths[1])

    elif command == "c":
        lengths = ask_for_lengths(
            "Enter the circle's radius", 1)
        circum, area = circle(lengths[0])

    return circum, area


def quit_program():
    """
    says "Goodbye!
    :return:
    """

    print("Goodbye!")


def incorrect_entry():
    """
    Prints "Incorrect entry, try again!" with a blank line
    :return:
    """
    print("Incorrect entry, try again!")
    print()


def main():
    # a value wich indicates that the program is running
    running = True

    while running:

        # get the command from user
        command = input("Enter the pattern's first letter or (q)uit: ")

        if command == "s" or command == "r" or command == "c":
            circum, area = check_for_cmd(command)
            print(f"The circumference is {circum:.2f}")
            print(f"The surface area is {area:.2f}")
            print()

        elif command == "q":
            quit_program()
            break

        else:
            incorrect_entry()
            continue




if __name__ == "__main__":
    main()
