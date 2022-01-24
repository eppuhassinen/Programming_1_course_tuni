"""
Tehtävä lukusarjapeli
Eppu Hassinen
Student number: 50044786
"""


def main():
    # this runs first in the program
    amount = int(input("How many numbers would you like to have? "))

    word_for_3 = "zip"
    word_for_7 = "boing"
    # this stores current loop
    i = 1

    # loops as many times as amount is set
    while i <= amount:
        if i % 3 == 0:
            if i % 7 == 0:
                print(word_for_3, word_for_7)
            else:
                print(word_for_3)
        elif i % 7 == 0:
            print(word_for_7)
        else:
            print(i)
        i += 1


if __name__ == "__main__":
    main()
