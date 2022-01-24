"""
Montako abbaa
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def longest_substring_in_order(text):
    """
    Checks for longest part where characters are in alphabetical order
    :param text: string, input
    :return: string, the longest alphabetical part of the input
    """
    # if the string is empty it returns itself
    if len(text) == 0:
        return text

    list_of_strigs = []
    alphabetical_part = text[0]

    for i in range(1, len(text)):

        # checks if the next character is bigger than the previous
        if alphabetical_part[len(alphabetical_part) - 1] < text[i]:
            # adds the next character to the part if it is bigger
            alphabetical_part += text[i]

            # does this when next character is not bigger than previous
        else:
            # puts a string of ordered chararacters to a list
            list_of_strigs.append(alphabetical_part)
            # makes the current character the start of next string
            alphabetical_part = text[i]

    # adds the last one to the list
    list_of_strigs.append(alphabetical_part)

    # checks which of the strings is longest and returns it
    longest_string = list_of_strigs[0]
    for n in list_of_strigs:

        if len(n) > len(longest_string):
            longest_string = n

    return longest_string
