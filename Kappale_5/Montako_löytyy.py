"""
Montako löytyy?
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def input_to_list(length_of_list):
    """
    Asks for numbers and stores them into a list
    :param length_of_list: int, the amount of numbers
    :return: list
    """

    print(f"Enter {length_of_list} numbers:")
    list_to_return = []

    # asks for numbers to the list
    for _ in range(length_of_list):
        list_to_return.append(int(input()))

    return list_to_return


def main():

    numbers_to_input = int(input("How many numbers do you want to process: "))
    numbers = input_to_list(numbers_to_input)
    number_to_search = int(input("Enter the number to be searched: "))

    amount: int = numbers.count(number_to_search)

    if amount > 0:
        print(f"{number_to_search} shows up {amount} times among the numbers "
              f"you have entered.")
    else:
        print(f"{number_to_search} is not among the numbers you have entered.")


if __name__ == '__main__':
    main()
