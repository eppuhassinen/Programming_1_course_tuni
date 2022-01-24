"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name:
Email:

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    while True:
        user_input = input("Enter product name: ")
        user_input = user_input.strip()
        if user_input == "":
            break
        elif user_input in PRICES:
            print(f"The price of {user_input} is {PRICES[user_input]:.2f}"
                  f" e")
        else:
            print(f"Error: {user_input} is unknown.")

    print("Bye!")


if __name__ == "__main__":
    main()
