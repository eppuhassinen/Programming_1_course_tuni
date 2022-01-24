"""
COMP.CS.100 Programming 1
Viestin luku
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def read_message():
    """
    Gets input and saves each line in different index in a list
    Stops when inputted an empty row
    :return: List, list of rows of text
    """
    list_of_rows = []
    while True:
        current_input = input()
        if current_input == "":
            return list_of_rows
        list_of_rows.append(current_input)


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for row in msg:
        print(row.upper())


if __name__ == "__main__":
    main()
