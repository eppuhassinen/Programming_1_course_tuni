"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
Eppu Hassinen
Student ID: 50044786
eppu.hassinen@tuni.fi
"""


class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    def __init__(self, name, hp=10):
        """
        Gives character a name and an empty inventory
        :param name: String, name to give.
        """
        self.__inventory = {}
        self.__name = name
        self.__hp = hp

    def give_item(self, item_to_give):
        """
        Adds item of type string to the dict as int 1
        :param item_to_give: string, item to add to inventory
        """
        if item_to_give in self.__inventory:
            self.__inventory[item_to_give] += 1
        else:
            self.__inventory[item_to_give] = 1

    def remove_item(self, item_to_remove):
        """
        Removes item if it is in the inventory
        :param item_to_remove: String, item to be removed
        """
        if item_to_remove in self.__inventory:
            if self.__inventory[item_to_remove] > 1:
                self.__inventory[item_to_remove] -= 1
            else:
                self.__inventory.pop(item_to_remove)

    def get_name(self):
        """
        :return: string, the name of character
        """
        return self.__name

    def how_many(self, item_to_calculate):
        """
        Counts how many times a value is in inventory
        :param item_to_calculate: string, item to calculate
        :return: int, how many times item was in inventory
        """
        if item_to_calculate in self.__inventory:
            return self.__inventory[item_to_calculate]
        return 0

    def printout(self):
        """
        Prints character name and inventory contents in alphabetical order
        """
        print(f"Name: {self.__name}")
        print(f"Hitpoints: {self.__hp}")

        if len(self.__inventory) == 0:
            print("  --nothing--")
            return

        for item in sorted(self.__inventory):
            print(f"  {self.__inventory[item]} {item}")

        return

    def has_item(self, item):
        """
        Checks if item is in inventory
        :param item: string, item to check
        :return: Boolean, True if item is found
        """
        return item in self.__inventory

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        if item not in self.__inventory:
            return False

        target.give_item(item)
        self.remove_item(item)
        return True

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        if weapon not in WEAPONS:
            print(f"""Attack fails: unknown weapon "{weapon}".""")
            return False

        if not self.has_item(weapon):
            print(f"""Attack fails: {self.__name} doesn't have "{weapon}".""")
            return False

        if self is target:
            print(f"Attack fails: {self.__name} can't attack him/herself.")
            return False

        print(f"{self.__name} attacks {target.__name} delivering"
              f" {WEAPONS[weapon]} damage.")

        target.__hp -= WEAPONS[weapon]
        if target.__hp <= 0:
            print(f"{self.__name} successfully defeats {target.__name}.")
        return True


WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
