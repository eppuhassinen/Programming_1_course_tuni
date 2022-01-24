"""
Rubikin kuutio kilpailu
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def ask_for_inputs(amount, sentence):
    """
    Asks for inputs and returns a list of them
    :param amount: amount of inputs
    :param sentence: sentence to say when asked an input
    :return: list of inputs
    """
    lst = []

    for i in range(amount):
        lst.append(float(input(f"{sentence} {i + 1}: ")))

    return lst


def competition_score(times):
    """
    Calculates the official score of the rubik's cube solving times in the list
    :param times: list of the times
    :return: float, in seconds
    """

    times.remove(max(times))
    times.remove(min(times))

    return sum(times) / len(times)


def main():
    # get the times as floats in a list
    times = ask_for_inputs(5, "Enter the time for performance")
    print(f"The official competition score "
          f"is {competition_score(times):.2f} seconds.")


if __name__ == '__main__':
    main()
