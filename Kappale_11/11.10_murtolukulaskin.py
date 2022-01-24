"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code
Eppu Hassinen
50044786
eppu.hassinen@tuni.fi
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    @property
    def simplify(self):
        """
        Simplifies the fraction by dividing numerator and denominator with
        their greatest common divisor
        :returns: a new fraction
        """
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)
        new_numerator = int(self.__numerator / divisor)
        new_denominator = int(self.__denominator / divisor)

        self.__numerator = new_numerator
        self.__denominator = new_denominator
        return

    def complement(self):
        """
        :returns: Fraction, as a complement to self
        """
        return Fraction(-self.__numerator, self.__denominator)

    def reciprocal(self):
        """
        :returns: Fraction, as a reciprocal to self
        """
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, other_fraction):
        """
        :param other_fraction: Fraction to multiply with
        :returns: Fraction as the multiplication of self and parameter
        """

        new_numerator = self.__numerator * other_fraction.__numerator
        new_denominator = self.__denominator * other_fraction.__denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other_fraction):
        """
        :param other_fraction: Fraction to divide with
        :returns: Fraction as the division of self and parameter
        """

        new_numerator = self.__numerator * other_fraction.__denominator
        new_denominator = self.__denominator * other_fraction.__numerator
        return Fraction(new_numerator, new_denominator)

    def add(self, other_fraction):
        """
        :param other_fraction: Fraction to add to self
        :returns: Fraction as the sum of two fractions
        """
        new_denominator = self.__denominator * other_fraction.__denominator
        new_numerator = (self.__numerator * other_fraction.__denominator) + \
                        (other_fraction.__numerator * self.__denominator)

        return Fraction(new_numerator, new_denominator)

    def deduct(self, other_fraction):
        """
        :param other_fraction: Fraction to deduct from self
        :returns: Fraction as the deduction of two fractions
        """
        new_denominator = self.__denominator * other_fraction.__denominator
        new_numerator = (self.__numerator * other_fraction.__denominator) - \
                        (other_fraction.__numerator * self.__denominator)
        return Fraction(new_numerator, new_denominator)

    def __lt__(self, other_fraction):
        return self.__numerator / self.__denominator < \
               other_fraction.__numerator / other_fraction.__denominator

    def __gt__(self, other_fraction):
        return self.__numerator / self.__denominator > \
               other_fraction.__numerator / other_fraction.__denominator

    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def add(fractions):
    """
    Adds a fraction to the dictionary
    :return: None
    """
    user_input = input("Enter a fraction in the form integer/integer: ")

    numerator, denominator = user_input.split("/")
    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        print(f"The fraction must in the form integer/integer."
              f" Your input was {user_input}")
        return
    name_input = input("Enter a name: ")

    fractions[name_input] = Fraction(numerator, denominator)

    return


def print_a_fraction(fractions):
    """
    Asks a name and prints the fraction if it exists
    """

    name_input = input("Enter a name: ")

    if name_input not in fractions:
        print(f"Name {name_input} was not found")
        return

    print(f"{name_input} = {fractions[name_input]}")


def print_a_list(fractions):
    """
    Prints all the fractions in a sorted list
    """
    if len(fractions) == 0:
        return
    for fraction in sorted(fractions):
        print(f"{fraction} = {fractions[fraction]}")


def multiply_fractions(fractions):
    """
    Asks for two fraction names and multiplies them if they exist
    """
    fraction_name1 = input("1st operand: ")
    if fraction_name1 not in fractions:
        print(f"Name {fraction_name1} was not found")
        return

    fraction_name2 = input("2nd operand: ")
    if fraction_name2 not in fractions:
        print(f"Name {fraction_name2} was not found")
        return

    product = fractions[fraction_name1].multiply(fractions[fraction_name2])
    print(f"{fractions[fraction_name1]} * "
          f"{fractions[fraction_name2]} = {product}")

    product.simplify

    print(f"simplified {product.return_string}")


def read_file(fractions):
    """
    Reads inputs from a file
    """
    file_name = input("Enter the name of the file: ")

    try:
        file = open(file_name, "r")
    except OSError:
        print("Error: the file cannot be read.")
        return

    try:
        for line in file:
            name, fraction_str = line.split("=")
            numerator, denominator = fraction_str.split("/")
            fractions[name] = Fraction(int(numerator), int(denominator))
    except ValueError:
        print("Error: the file cannot be read.")


def user_interface():
    """
    Checks for user commands and runs the commands
    """
    fractions = {}

    while True:
        user_input = input("> ")

        if user_input == "quit":
            print("Bye bye!")
            return

        if user_input == "add":
            add(fractions)
            continue

        if user_input == "print":
            print_a_fraction(fractions)
            continue

        if user_input == "list":
            print_a_list(fractions)
            continue

        if user_input == "*":
            multiply_fractions(fractions)
            continue

        if user_input == "file":
            read_file(fractions)
            continue

        else:
            print("Unknown command!")


def main():

    user_interface()


if __name__ == '__main__':
    main()
