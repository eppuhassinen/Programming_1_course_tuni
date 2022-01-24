"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__weight_info = Label(self.__mainwindow, text="Weight (kg)")
        self.__height_info = Label(self.__mainwindow, text="Height (cm)")
        self.__bmi_info = Label(self.__mainwindow, text="BMI: ")

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="Calculate",
                                         command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text="")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Quit",
                                    command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_info.grid(row=1, column=0)
        self.__height_info.grid(row=2, column=0)
        self.__weight_value.grid(row=1, column=1, sticky=W)
        self.__height_value.grid(row=2, column=1, sticky=W)
        self.__calculate_button.grid(row=3, column=1, columnspan=2, sticky=W)
        self.__stop_button.grid(row=10, column=15, sticky=E)
        self.__bmi_info.grid(row=4, column=0, sticky=E)
        self.__result_text.grid(row=4, column=1, sticky=W)
        self.__explanation_text.grid(row=5, column=1, sticky=W)

        self.__mainwindow.mainloop()

    def check_float(self, value):
        """
        :param value: anything
        :return: float, if input can be converted to float, otherwise None
        """

        try:
            tested_value = float(value)
            return tested_value
        except ValueError:
            return None

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        weight = self.__weight_value.get()
        height = self.__height_value.get()

        weight = self.check_float(weight)
        height = self.check_float(height)

        # error checking
        if weight is None or height is None:
            self.__explanation_text['text'] = "Error: height and weight " \
                                              "must be numbers."
            self.reset_fields()
            return

        if weight <= 0 or height <= 0:
            self.__explanation_text['text'] = "Error: height and weight " \
                                              "must be positive."
            self.reset_fields()
            return

        # cm to m
        height = height / 100

        bmi = weight / pow(height, 2)
        self.__result_text['text'] = f"{bmi:.2f}"

        if bmi > 25:
            self.__explanation_text['text'] = "You are overweight."
        elif bmi >= 18.5:
            self.__explanation_text['text'] = "Your weight is normal."
        else:
            self.__explanation_text['text'] = "You are underweight."

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__result_text['text'] = ""
        self.__weight_value.delete(0, END)
        self.__height_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
