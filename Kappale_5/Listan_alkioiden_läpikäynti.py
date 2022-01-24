"""
Lukujonoja
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def main():

    print("Give 5 numbers:")

    numbers = []

    for _ in range(5):
        n = int(input("Next number: "))
        numbers.append(n)

    print("The numbers you entered that were greater than zero were:")

    for value in numbers:
        if value > 0:
            print(value)


if __name__ == '__main__':
    main()
