"""
Fibonaccin lukusarja
Eppu Hassinen
Student number: 50044786
"""


def main():
    amount_of_numbers = int(input("How many Fibonacci numbers do you want? "))

    i = 1
    current_n = 1
    previous_n = 0
    previous_n_2 = 0
    while i <= amount_of_numbers:

        print(i, ". ", current_n, sep="")
        previous_n = current_n
        current_n = previous_n + previous_n_2
        previous_n_2 = previous_n

        i += 1


if __name__ == "__main__":
    main()
