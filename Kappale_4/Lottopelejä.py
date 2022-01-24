"""
Lottopelejä
Nimi: Eppu Hassinen
Opiskelijanumero: 50044786
"""
import math


def check_numbers(total, drawn):

    """
    Checks if any of the numbers is negative and prints it to the user
    Checks if the amount of drawn balls is bigger than the amount of total
    balls and prints the error to the user

    :param total: int, amount of total balls
    :param drawn: int, amount of balls to draw
    :return: true if ok
    """

    for n in [total, drawn]:
        if n <= 0:
            print("The number of balls must be a positive number.")
            return None

    if drawn > total:
        print("At most the total number of balls can be drawn.")
        return None

    return True


def possibilities(total, drawn):
    """
    Calculates the amount of different possibilities of drawing x amount of
    random balls
    :param total: int, the total amount of balls
    :param drawn: int, the amount of balls drawn
    :return: float, the amount
    """

    # calculates the possibilities: n! / ((n-p)! * p!
    # where n is total and p is drawn
    n = math.factorial(total) / ((math.factorial(total - drawn)) *
                                 math.factorial(drawn))
    return int(n)


def main():

    total_balls = int(input("Enter the total number of lottery balls: "))
    balls_drawn = int(input("Enter the number of the drawn balls: "))

    # Stops and returns None if numbercheck returns None
    if not check_numbers(total_balls, balls_drawn):
        return None

    print(f"The probability of guessing all {balls_drawn} balls correctly "
          f"is 1/{possibilities(total_balls, balls_drawn)}")


if __name__ == "__main__":
    main()
