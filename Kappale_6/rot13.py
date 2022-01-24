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


