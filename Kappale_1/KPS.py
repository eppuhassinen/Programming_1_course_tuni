"""
COMP.CS100 Greeting tehtävä
Tekijä: Eppu Hassinen
Opiskelijanumero: 50044786
"""


def main():
    player_1 = input("Player 1, enter your choice (R/P/S): ")
    player_2 = input("Player 2, enter your choice (R/P/S): ")

    if player_1 == player_2:
        print("It's a tie!")
    elif player_1 == "R" and player_2 == "S":
        print("Player 1 won!")
    elif player_1 == "P" and player_2 == "R":
        print("Player 1 won!")
    elif player_1 == "S" and player_2 == "P":
        print("Player 1 won!")
    else:
        print("Player 2 won!")


if __name__ == "__main__":
    main()
