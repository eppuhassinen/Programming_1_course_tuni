"""
Numeroiden ja rivien kirjoittaminen tiedostoon
Eppu Hassinen
50044786
"""


def main():
    file_name = input("Enter the name of the file: ")

    try:
        file = open(file_name, mode="w")
        # stores the line number
        i = 1

        print("Enter rows of text. Quit by entering an empty row.")
        text_list = read_message()

        for i in range(len(text_list)):
            print(f"{i + 1} {text_list[i]}", file=file)

        file.close()

        print(f"File {file_name} has been written.")

    except OSError:
        print(f"Writing the file {file_name} was not successful.")


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


if __name__ == '__main__':
    main()
