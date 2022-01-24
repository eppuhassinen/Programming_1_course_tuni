"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
Eppu Hassinen
Student ID: 50044786
eppu.hassinen@tuni.fi
"""


class Character:

    def __init__(self, name):
        """
        Gives character a name and an empty inventory
        :param name: String, name to give.
        """
        self.__inventory = {}
        self.__name = name

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


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
