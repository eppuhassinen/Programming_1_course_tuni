"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Code template for a simplified car assignment
implementation using a class.
Eppu Hassinen
eppu.hassinen@tuni.fi
50044786
"""


class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = 0
        self.__odometer = 0

        # create and initialize the rest of the attributes.

    def print_information(self):
        """
        Prints the amount of gas and odometer in this format:
        The tank contains 0.0 liters of gas and the \
        odometer shows 0.0 kilometers.
        :return:
        """
        print(f"The tank contains {self.__gas:.1f} liters of gas "
              f"and the odometer shows {self.__odometer:.1f} kilometers.")

    def fill(self, amount_of_gas):
        """
        Adds gas to the tank. If amount is neagtive it gives an error.
        Maximum amount is the size of the tank
        :param amount_of_gas: float, amount of gas to add
        :return:
        """

        if amount_of_gas < 0:
            raise ValueError("You cannot remove gas from the tank")

        self.__gas += amount_of_gas
        if self.__gas > self.__tank_volume:
            self.__gas = self.__tank_volume

    def drive(self, distance):
        """
        Removes used gas from the tank
        :param distance: float, distance driven
        :return:
        """
        if distance < 0:
            raise ValueError("You cannot travel a negative distance")

        used_gas = distance * self.__consumption * 0.01
        if used_gas > self.__gas:
            self.__odometer += self.__gas / (self.__consumption * 0.01)
            self.__gas = 0
        else:
            self.__gas -= used_gas
            self.__odometer += distance


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    # Here we define the variable car which is an object initiated
    # from the class Car (its type is Car). This is the point where the
    # constructor of the class Car (i.e. the method that is named __init__)
    # is called automatically behind the scenes to give an initial
    # value for the Car object we are creating!

    car = Car(tank_size, gas_consumption)

    # In this program we only need one car object but it is possible
    # to create multiple objects from one class. For example we could
    # create more objects if we needed them:
    #
    #     lightning_mcqueen = Car(20, 30)
    #     canyonero = Car(200, 400)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")

            try:
                car.fill(to_fill)
            except ValueError as error_message:
                print(error_message)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")

            try:
                car.drive(distance)
            except ValueError as error_message:
                print(error_message)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
