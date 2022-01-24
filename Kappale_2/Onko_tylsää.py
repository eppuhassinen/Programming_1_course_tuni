"""
Onko tylsää asks if the user is bored and stops if true
Eppu Hassinen
Student number: 50044786
"""


def main():
    # the program starts here
    value = True

    # asks if bored until input is "y"
    while value:

        user_input = input("Bored? (y/n) ")

        if (user_input != "Y" and user_input != "N" and user_input != "y"
                and user_input != "n"):
            print("Incorrect entry.")
        elif user_input == "y" or user_input == "Y":
            print("Well, let's stop this, then.")
            value = False


if __name__ == "__main__":
    main()
