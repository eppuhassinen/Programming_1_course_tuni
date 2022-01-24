"""
COMP.CS100 Greeting tehtävä
Tekijä: Eppu Hassinen
Opiskelijanumero: 50044786
"""

raise_percent = 1.0117
# asks for amount
amount = float(input("Enter the amount of the study benefits: "))

print("If the index raise is 1.17 percent, the study benefit,")
amount = amount * raise_percent
print("after a raise, would be", amount, "euros")
print("and if there was another index raise, the study")
amount = amount * raise_percent
print("benefits would be as much as", amount, "euros")


