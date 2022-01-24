"""
Vokaalilastkuri
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def main():
    word = input("Enter a word: ")

    vowels = "aeiouy"
    consonant_count = 0
    vowel_count = 0

    for letter in word:
        for vowel in vowels:
            if letter == vowel:
                vowel_count += 1
                continue

    consonant_count = len(word) - vowel_count

    print(f"""The word "{word}" contains {vowel_count} vowels and \
{consonant_count} consonants.""")


if __name__ == '__main__':
    main()
