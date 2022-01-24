"""
COMP.CS100 Greeting tehtävä
Tekijä: Eppu Hassinen
Opiskelijanumero: 50044786
"""


def main():
    mood = input("How do you feel? (1-10) ")
    mood = int(mood)
    if 1 <= mood <= 10:
        if mood == 10:
            print("A suitable smiley would be :-D")
        elif mood > 7:
            print("A suitable smiley would be :-)")
        elif mood >= 4:
            print("A suitable smiley would be :-|")
        elif mood > 1:
            print("A suitable smiley would be :-(")
        else:
            print("A suitable smiley would be :'(")
    else:
        print("Bad input!")


if __name__ == "__main__":
    main()
