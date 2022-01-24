"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.

Eppu Hassinen
Opiskelijanumero: 50044786
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {}

    for n in english_spanish:
        spanish_english[english_spanish[n]] = n

    print("Dictionary contents:")
    print(", ".join(sorted(english_spanish)))
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print(f"The word {word} could not"
                      f" be found from the dictionary.")

        elif command == "A":

            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")

            english_spanish[english_word] = spanish_word
            spanish_english[spanish_word] = english_word

            print("Dictionary contents:")
            print(", ".join(sorted(english_spanish)))

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del(english_spanish[word])
            else:
                print(f"The word {word} could not be found from "
                      f"the dictionary.")

        elif command == "P":
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])

            print()
            print("Spanish-English")
            for word in sorted(spanish_english):
                print(word, spanish_english[word])

            print()

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            text_list = text.split()
            print("The text, translated by the dictionary:")
            translated_text = ""
            for word in text_list:
                if word in english_spanish:
                    translated_text += english_spanish[word] + " "
                else:
                    translated_text += word + " "
            translated_text.rsplit()
            print(translated_text)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
