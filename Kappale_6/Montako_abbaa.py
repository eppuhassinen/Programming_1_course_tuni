"""
Montako abbaa
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def count_abbas(text):
    """
    Counts how many times the string abba is in the text
    Abbas can be on top of eachother
    :param text: string, text to analyze
    :return: int, times abba was in the text
    """

    word_to_find = "abba"
    amount_of_words = 0

    # checks for the words in the text
    for letter in range((len(text) - len(word_to_find)) + 1):
        correct = 0
        for i in range(len(word_to_find)):
            if text[letter + i] == word_to_find[i]:
                correct += 1
            if correct == len(word_to_find):
                amount_of_words += 1

    return amount_of_words
