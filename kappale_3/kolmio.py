"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
Eppu Hassinen
Opiskelijanumero: 50044786
"""
import math
from math import sqrt


def area(a, b, c):
    """
    Calculates the area of a triangle
    :param a: first side length
    :param b: second side lenth
    :param c: third side length
    :return: the area
    """

    # s is half of the radius
    s = (a + b + c) / 2

    # calculates the area
    value = sqrt(s * (s - a) * (s - b) * (s - c))
    return value


def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    triangle_area: float = area(a, b, c)

    print(f"The triangle's area is {triangle_area:.1f}")


if __name__ == "__main__":
    main()
