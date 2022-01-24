"""
Ohjelmointi 1 Kappale 6 Tilastointia -projekti
Nimi: Eppu Hassinen
Opiskelijanumero: 50044786

Program asks for inputs
Prints the mean of the data
Prints the standard deviation of the data
Prints a simple histogram of the data around the standard deviation
"""
import math

# the amount of different ranges in the histogram
histogram_length = 6
# the width multiplier of the ranges in the histogram
histogram_range_width = 1
# offset of the histogram
histogram_offset = 0


def main():
    # reads the inputs from the user and stores the list
    values = read_inputs()

    # checks if values is None and stops the program
    if values is None:
        return None

    # stores the mean and deviation
    mean, deviation = mean_deviation(values)

    print(f"The mean of given data was: {mean:.2f}")

    print(f"The standard deviation of given data was: {deviation:.2f}")

    if deviation == 0:
        print("Deviation is zero.")
        return None

    # prints the histogram
    histogram(values, histogram_length, deviation)


def read_inputs():
    """
    Reads inputs from the user. Inputs may be floats or integers.
    Reading stops if the input is blank line.
    Returns None and prints an error message if there is less than two values
    :return: List, list with numbers
    """

    print("Enter the data, one value per line.")
    print("End by entering empty line.")

    # list to store the numbers
    values = []

    while True:
        value = input()

        # checks for empty input
        if value == "":
            if len(values) > 1:
                return values

            # Prints an error if not enough values
            print("Error: needs two or more values.")
            return None

        # converts value to float and puts it in the list
        values.append(float(value))


def mean_deviation(values):
    """
    Calculates the mean and standard deviation of the list
    :param values: List, list of floats
    :return: float, mean; float, standard deviation
    """

    mean = sum(values) / len(values)

    # number to store a part of the expression
    # variance = (1 / (N - 1)) * ((N_0 - mean)^2 + (N_1 - mean)^2 ...)
    n = 0
    for i in values:
        n += math.pow((i - mean), 2)
    variance = (1 / (len(values) - 1)) * n

    # stores the standard deviation
    deviation = math.sqrt(variance)

    return mean, deviation


def histogram(values, amount, deviation):
    """
    Prints a histogram from "amount" categories:
    categories are:
    category 0: 0.0 to 0.5 * "deviation"
    category 1: 0.5 * "deviation" to 1.0 * "deviation"
    ...
    category "amount": X.X * "deviation" to X.X * "deviation"

    Each index in "values" gets placed in one of the categories like this
    |values[x] - mean|
    :param values: list, floats
    :param amount: int, amount of categories
    :param deviation: float, deviation of the values in list
    :return: none
    """

    for category_number in range(0, amount):
        minimum = (category_number * histogram_range_width * 0.5 *
                   deviation) + histogram_offset
        maximum = ((category_number + 1) *
                   histogram_range_width * 0.5 * deviation) + histogram_offset

        height = calculate_amount_in_range(values, minimum, maximum) * "*"

        print(
            f"Values between std. dev. {minimum:.2f}-{maximum:.2f}: {height}")


def calculate_amount_in_range(values, minim, maxim):
    """
    Calculates how many |members of the list - mean of the list| is in
    the given range
    :param values: list, floats
    :param minim: float, minimum
    :param maxim: float, maximum
    :return: int, amount
    """
    # int to store the amount
    amount = 0

    # mean of the list
    mean = sum(values) / len(values)

    # checks how many |value - mean| are in the range
    for i in values:
        n = abs(i - mean)
        if n >= minim:
            if n < maxim:
                amount += 1

    return amount


if __name__ == '__main__':
    main()
