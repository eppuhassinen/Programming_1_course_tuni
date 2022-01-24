"""
Kertotaulu tehtävä yli sadan
Eppu Hassinen
Student number: 50044786
"""


def main():
    # this runs first in the program
    number = int(input("Choose a number: "))

    # how many numbers we want to calculate
    over_100 = False

    # loop to calculate and print the calculations until the value is > 100
    i = 1
    while i * number <= 100:
        print(i, "*", number, "=", i * number)
        i += 1

    # prints once after its greater than 100
    print(i, "*", number, "=", i * number)


if __name__ == "__main__":
    main()
