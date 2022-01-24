"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 50044786
Name:       Eppu Hassinen
Email:      eppu.hassinen@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):

        self.__main_window = Tk()

        self.__current_value = 0
        # Label displaying the current value of the counter.
        self.__current_value_label = Label(self.__main_window,
                                           text=self.__current_value,)
        self.__current_value_label.grid(row=0, column=0, columnspan=4,
                                        sticky=N+S)

        # Button which resets counter to zero.
        self.__reset_button = Button(self.__main_window, text="Reset",
                                     command=self.reset)
        self.__reset_button.grid(row=1, column=0)

        # Button which increases the value of the counter by one.
        self.__increase_button = Button(self.__main_window, text="Increase",
                                        command=self.increase)
        self.__increase_button.grid(row=1, column=1)

        # Button which decreases the value of the counter by one.
        self.__decrease_button = Button(self.__main_window, text="Decrease",
                                        command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)

        # Button which quits the program.
        self.__quit_button = Button(self.__main_window, text="Quit",
                                    command=self.quit)
        self.__quit_button.grid(row=1, column=3)

        self.__main_window.mainloop()

    def increase(self):
        """
        increases the value by 1
        :return:
        """
        self.__current_value += 1
        self.__current_value_label['text'] = self.__current_value

    def decrease(self):
        """
        decreases the value by 1
        :return:
        """
        self.__current_value -= 1
        self.__current_value_label['text'] = self.__current_value

    def reset(self):
        """
        makes value 0
        :return:
        """
        self.__current_value = 0
        self.__current_value_label['text'] = self.__current_value

    def quit(self):
        """
        Quits program
        """
        self.__main_window.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
