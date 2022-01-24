"""
COMP.CS.100 Programming 1
ROT13 encryption
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # TODO: implement encryption here

    for key in range(len(regular_chars)):
        if text == regular_chars[key]:
            return encrypted_chars[key]

        elif text == regular_chars[key].upper():
            return encrypted_chars[key].upper()

    return text


def row_encryption(text):
    """
    Encrypts whole sentences of text by encrypting one letter at a time
    calling encrypt() funktion
    :param text: string, text to encrypt
    :return: string, encrypted text
    """
    encrypted_text = ""

    for n in text:
        encrypted_text += encrypt(n)

    return encrypted_text


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

    print("ROT13:")
    for row in msg:
        print(row_encryption(row))


if __name__ == "__main__":
    main()
