"""
Sanatiheyslaskuri
Eppu Hassinen
50044786
"""


def get_input():
    """
    Reads input from the user and returns all rows in one string
    :return: string, user input
    """
    text = ""

    while True:
        row = input()
        if row == "":
            return text
        text += " " + row


def main():

    print("Enter rows of text for word counting. Empty row to quit.")
    text = get_input()
    text = text.lower()
    words = text.split()
    word_counter = {}

    # calculates the words
    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    for word in sorted(word_counter):
        print(f"{word} : {word_counter[word]} times")


if __name__ == '__main__':
    main()
