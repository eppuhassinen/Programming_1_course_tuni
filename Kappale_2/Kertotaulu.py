"""
Kertotaulu tehtävä
Eppu Hassinen
Student number: 50044786
"""


def main():
    # this runs first in the program
    number = int(input("Choose a number: "))

    # how many numbers we want to calculate
    amount_of_numbers = 10

    # loop to calculate and print the calculations
    i = 1
    while i <= amount_of_numbers:
        print(i, "*", number, "=", i * number)
        i += 1


if __name__ == "__main__":
    main()
