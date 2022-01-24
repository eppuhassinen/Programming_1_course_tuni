"""
Prints all fridays of a year
Eppu Hassinen
Student number: 50044786
"""


def main():
    # the program starts here
    month = 1
    # is used to set the first friday of the year
    # first friday was 3.1. so day counter is set to 5
    day_counter = 5
    # days in months
    list_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while month <= 12:
        day = 1
        while day <= list_of_days[month - 1]:
            if day_counter % 7 == 0:
                print(day, ".", month, ".", sep="")
            day += 1
            day_counter += 1
        month += 1


if __name__ == "__main__":
    main()
