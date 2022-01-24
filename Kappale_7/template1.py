"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 50044786
Name: Eppu Hassinen
Email: eppu.hassinen@tuni.fi

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def payload(key):
    """
    Returns the value from "PRICES" dict
    :param key: str
    :return: float, the value
    """
    return PRICES[key]


def main():

    sorted_list = sorted(PRICES, key=payload)

    for n in sorted_list:
        print(f"{n} {PRICES[n]:.2f}")


if __name__ == "__main__":
    main()
