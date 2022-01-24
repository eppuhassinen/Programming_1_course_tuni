"""
COMP.CS100 Vaihtorahat
ja maksusta
Tekijä: Eppu Hassinen
Opiskelijanumero: 50044786
"""

# tulostaa vaihtorahat mikäli kyseistä rahaa on yli 0
def changeprint(amount, note):
    """tulostaa vaihtorahat mikäli kyseistä rahaa on yli 0"""
    # tulostaa vaihtorahat mikäli kyseistä rahaa on yli 0
    if amount > 0:
        print(amount, note)
    return


def main():
    # Price
    price = int(input("Purchase price: "))
    # Paid money
    money = int(input("Paid amount of money: "))
    # Calculate the change
    change = money - price

    if change <= 0:
        print("No change")
    else:
        print("Offer change:")

    # calculate the amount of 10s and store the amount
    ten = change // 10
    # subtract tens from the change
    change = change - (ten * 10)

    # calculate the amount of 5s and store the amount
    five = change // 5
    # subtract tens from the change
    change = change - (five * 5)

    # calculate the amount of 2s and store the amount
    two = change // 2
    # subtract tens from the change
    change = change - (two * 2)

    # print the change amounts

    # tulostaa kyseiset luvut
    changeprint(ten, "ten-euro notes")
    # tulostaa kyseiset luvut
    changeprint(five, "five-euro notes")
    # tulostaa kyseiset luvut
    changeprint(two, "two-euro coins")
    # tulostaa kyseiset luvut
    changeprint(change, "one-euro coins")


if __name__ == "__main__":
    main()
