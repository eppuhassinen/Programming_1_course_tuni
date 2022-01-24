"""
Lenkkiprojekti
Eppu Hassinen
Student number: 50044786
"""


def main():
    # asks the amount of days
    number_of_days = int(input("Enter the number of days: "))

    # makes a list with a length from the amount of days
    km_run = [0] * number_of_days

    # a boolean value for 3 or more consecutive days without running
    lazy = False

    # counter for days without running
    zero_counter = 0
    # asks for running lengths per day
    i = 1
    while i <= number_of_days:
        print("Enter day", i, "running length: ", end="")
        km_run[i-1] = float(input())

        # checks for consecutive days without running
        if km_run[i - 1] != 0:
            zero_counter = 0

        else:
            zero_counter += 1
            if zero_counter >= 3:
                lazy = True
                break
        i += 1

    mean_of_kilometers = sum(km_run) / number_of_days

    # prints the right output according to running mean
    print()
    if lazy:
        print("You had too many consecutive lazy days!")

    elif mean_of_kilometers >= 3:
        print("You were persistent runner! ", end="")
        print(f"With a mean of {mean_of_kilometers:.2f} km.")

    elif mean_of_kilometers < 3:
        print(f"Your running mean of {mean_of_kilometers:.2f} km was too low!")

    else:
        print("Something went wrong!")


if __name__ == "__main__":
    main()


