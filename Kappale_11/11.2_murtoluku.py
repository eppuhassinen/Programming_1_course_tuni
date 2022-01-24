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

    def simplify(self):
        """
        Simplifies the fraction by dividing numerator and denominator with
        their greatest common divisor
        """
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator / divisor)
        self.__denominator = int(self.__denominator / divisor)

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
        other_numerator, other_denominator = \
            other_fraction.return_string.split("/")

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

def read_inputs_to_fractions():
    """
    :return: List, list of fractions
    """
    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")

    fractions = []

    while True:
        fraction_str = input()
        if fraction_str == "":
            return fractions

        new_numerator, new_denominator = fraction_str.split("/")
        fractions.append(Fraction(int(new_numerator), int(new_denominator)))

def main():

    input_fractions = read_inputs_to_fractions()

    print("The given fractions in their simplified form:")
    for fraction in input_fractions:
        original = fraction.return_string()
        fraction.simplify()
        simplified = fraction.return_string()
        print(f"{original} = {simplified}")


if __name__ == '__main__':
    main()
