"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
This is a writing game.
It reads words it is going to use from a txt file. File needs to be in
english because python doesn't like ä's and ö's.
File opener automatically deletes spaces and marks as . , : from the
end of the words

Eppu Hassinen
Student ID: 50044786
eppu.hassinen@tuni.fi
"""
import time
import random


def play(words):
    """
    The actual game happens here.
    :param words: List, list of words in english
    :return: None
    """

    # checks for correct input to avoid errors
    while True:
        try:
            # amount of words in each line in the next game
            words_in_line = int(input("Enter how many words you "
                                      "want in a row: "))

            # amount of lines in the next game
            total_lines = int(input("Enter the total amount of rows"
                                    " you want to type: "))
            # breaks out of the loop when inputs are correct
            break

        except ValueError:
            print("Incorrect input!")
            print()

    # total word amount in the list
    word_amount = len(words)
    # integers to store numbers for score calculation
    right_words = 0
    total_words = 0
    words_per_sec = 0
    correct_words_percent = 0

    # countdown to start
    print("Ready...")
    time.sleep(1)
    print("Set...")
    time.sleep(1)
    print("Go!")
    # save start time so it is possible to calculate time from this moment
    start_time = time.time()

    # loop for the actual game
    # loops for each user specified line
    for _ in range(total_lines):

        # empty list to store each generated line
        line = []

        # generates random line
        for _ in range(words_in_line):
            line.append(words[random.randrange(word_amount)])

        # prints the generated line with an empty row
        for word in line:
            print(f"{word} ", end="")
        print()
        print()

        # takes user input for current line
        line_input = input()
        # makes user input into a list so it's easier to compare each word to
        # the computer made line
        input_words = line_input.strip().split(" ")

        # Checking wich one is shorter to avoid errors
        length = words_in_line
        if len(input_words) < words_in_line:
            length = len(input_words)

        # Calculating the score
        i = 0
        while i < length:

            # if word is correct add 1 to right_words calculator
            if line[i] == input_words[i]:
                right_words += 1

            i += 1
        # adds words in the line to total counter
        total_words += words_in_line

        # calculating time related stuff
        words_per_sec = right_words / (time.time() - start_time)
        correct_words_percent = (right_words / total_words) * 100

        # prints in the middle of the game, so player can keep an eye on
        # his/her progression
        print(f"{words_per_sec:.2f} words per sec, "
              f"{correct_words_percent:.0f}% correct")

    # Prints this when finished
    print(f"You wrote correct {right_words} words out of {total_words} words!")
    print(f"That is {correct_words_percent} % correct")
    print(f"Total time was {(time.time() - start_time):.2f}")
    print(f"Average speed was {words_per_sec:.2f} words/s")


def load_from_file():
    """
    Asks the user for a file name.
    Saves words from a text file in a list and returns it.
    Function also deletes marks as . , from the end of words
    :return: List, full of words
    """
    file_name = input("Enter file name: ")
    try:
        file = open(file_name, mode="r")
    except OSError:
        print(f"There was a problem opening file: '{file_name}'.")
        return None

    words = []

    for line in file:
        for word in line.split(" "):
            word = word.strip()
            words.append(word)

    file.close()

    print("File reading successful")
    return words


def user_interface():
    """
    Runs the user commands and is the heart of the program.
    :return: None
    """

    # commands in a dict for simplicity
    COMMANDS = {
                "help": "view all commands",
                "open": "open a text file",
                "start": "start the game",
                "quit": "quit"
                }

    # list to store words
    words = []

    # runs the commands
    while True:
        print()
        print("Enter command. Type 'help' for help")
        command = input("> ")

        if command == "help":

            print(f"This is a speed writing game where you can use your own "
                  f"words.")
            print(f"Make a text file where is english words and open it "
                  f"in this program.")

            for comm in COMMANDS:
                print(f"Enter '{comm}' to {COMMANDS[comm]}.")

        if command == "quit":
            print("Quitting..")
            return

        if command == "open":
            words = load_from_file()

        if command == "start":

            # checks if there is words in memory
            if len(words) == 0:
                print("No words in memory. Use command 'open' to load words "
                      "from a text file.")
                continue

            # if there is few words asks the program if user wants to continue
            if len(words) < 30:
                print(f"Your word file had only {len(words)} words. Do you "
                      f"wish to continue? Type 'y' yes or 'n' no")

                new_input = input("> ")

                if new_input == "y":
                    pass

                elif new_input == "n":
                    continue

                else:
                    print("Unknown command!")

            # if we got here everything is good to start a game
            play(words)


def main():

    print("Welcome to speed writer by: Eppu Hassinen")
    user_interface()


if __name__ == '__main__':
    main()
