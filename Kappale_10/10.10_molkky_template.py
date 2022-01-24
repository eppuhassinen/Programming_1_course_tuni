"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
Eppu Hassinen
eppu.hassinen@tuni.fi
50044786
"""


# TODO:
# a) Implement the class Player here.
class Player:

    def __init__(self, name, start_points=0):
        """
        :param name: name of player
        :param start_points: int, usually 0
        """

        self.__name = name
        self.__points = start_points
        self.__throw_counter = 0
        self.__total_points = self.__points
        self.__hit_counter = 0

    def get_name(self):
        """
        :return: str, player name
        """
        return self.__name

    def get_points(self):
        """
        :return: int, current points
        """
        return self.__points

    def has_won(self):
        """
        Checks if player has 50 points
        :return: Boolean, true if won
        """
        if self.__points == 50:
            return True
        return False

    def add_points(self, points_to_add):
        """
        Adds points. If over 50 gets set to 25
        :param points_to_add: int, points to add
        :return:
        """
        self.__throw_counter += 1
        self.__points += points_to_add
        self.__total_points += points_to_add
        if self.__points > 50:
            print(f"{self.__name} gets penalty points!")
            self.__points = 25
        if 40 <= self.__points <= 49:
            print(f"{self.__name} needs only {50 - self.__points} points. "
                  f"It's better to avoid knocking down the pins with "
                  f"higher points.")
        if points_to_add > 0:
            self.__hit_counter += 1

    def mean_of_throws(self):
        """
        Calculates the mean of all player's throws
        :return: float, mean
        """
        return self.__total_points / self.__throw_counter

    def hit_percent(self):
        """
        :return: float, hit percentage
        """
        if self.__throw_counter == 0:
            return 0
        return (self.__hit_counter / self.__throw_counter) * 100


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if pts > in_turn.mean_of_throws():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,"
              " hit percentage " + f"{player1.hit_percent():.1f}")
        print(player2.get_name() + ":", player2.get_points(), "p,"
              " hit percentage " + f"{player2.hit_percent():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
