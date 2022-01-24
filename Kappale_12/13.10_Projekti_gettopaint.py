"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This is a program where you can draw circles in a grid
The color and the radius of the circles can be changed in the user interface
Grid size can be changed here in the code.

Eppu Hassinen
Student ID: 50044786
eppu.hassinen@tuni.fi
"""

import math
from functools import partial
from tkinter import *

# size of the game can be changed here
# All buttons should behave good if you don't go below 16
# if you go too big it gets slow and impossible to read the text
GAME_SIZE = 30


class Coordinates:
    """
    class contains a 2 dimensional array that stores 1s and 0s
    [
        [0, 0, 0, 0, 0], 0# rows are y coordinates
        [0, 0, 0, 0, 0], 1#
        [0, 0, 0, 0, 0], 2#
        [0, 0, 0, 0, 0], 3#
        [0, 0, 0, 0, 0], 4#
    ]    0  1  2  3  4  indexes in rows are x coordinates

        the matrix is read: list[y][x]

    """

    def __init__(self):
        # initializes the array
        self.__coordinates = []

        # makes the array square and right sized
        for i in range(GAME_SIZE):
            self.__coordinates.append(list([0] * GAME_SIZE))

    def get_coordinates(self):
        """
        :returns: list, the array that contains all the information.
        """

        return self.__coordinates

    def circle(self, center, radius):
        """
        Changes all the values that are in self.__coordinates wich are in
        the circle with specified radius.
        Changes all 1s to 0s and 0s to 1s
        :param center: tuple int, center of the circle
        :param radius: float, radius of the circle
        :return: Returns True if all went okay
        """

        # store center point to simpler format
        center_x, center_y = center

        # loops through the matrix
        y = 0

        while y < len(self.__coordinates):
            x = 0
            while x < len(self.__coordinates[y]):
                # checks if the distance is smaller than radius
                if get_distance((center_x, center_y), (x, y)) < radius:

                    # 0's to 1's and 1's to 0's
                    self.__coordinates[y][x] = \
                        abs(self.__coordinates[y][x] - 1)
                x += 1
            y += 1

        return True

    def reset(self):
        """
        resets all values to 0
        :return:
        """
        # loops through the matrix
        y = 0

        while y < len(self.__coordinates):
            x = 0
            while x < len(self.__coordinates[y]):

                # makes everything 0
                self.__coordinates[x][y] = 0
                x += 1
            y += 1


class Userinterface:

    def __init__(self):

        self.__mainw = Tk()
        self.__mainw.title(f"Gettopaint")
        self.__mainw.option_add("*Font", f"Verdana {int(250 / GAME_SIZE)}")

        self.__game_field = []

        # makes the Buttons for the program in similar matrix than in
        # class Coordinates
        for i in range(GAME_SIZE):
            self.__game_field.append([] * GAME_SIZE)

        # loops through all buttons
        y = 0

        while y < len(self.__game_field):
            x = 0
            while x < GAME_SIZE:

                # makes uniquie attributes for the command for each button
                self.__game_field[y].append(Button(background="#FFFFFF",
                                                   text="   ",
                                                   command=partial
                                                   (self.click, x, y)))

                self.__game_field[y][x].grid(row=y + 1, column=x + 1)
                x += 1
            y += 1

        # basic interface stuff
        # quit button
        self.__quit_button = Button(background="red", relief=RAISED,
                                    borderwidth=5, text="Quit",
                                    command=self.stop)
        self.__quit_button.grid(row=GAME_SIZE + 2, column=GAME_SIZE - 2,
                                sticky=E, columnspan=3)

        # reset button
        self.__reset_button = Button(background="green", relief=RAISED,
                                     borderwidth=5, text="Reset",
                                     command=self.reset)
        self.__reset_button.grid(row=GAME_SIZE + 3, column=GAME_SIZE - 2,
                                 sticky=E, columnspan=3)

        # radius changing stuff
        self.__radius_info = Label(text="Radius \n (positive)")
        self.__radius_info.grid(row=GAME_SIZE + 2, column=1,
                                sticky=W, columnspan=8)

        self.__radius_entry = Entry(background="white",
                                    borderwidth=5, text="Right")
        self.__radius_entry.grid(row=GAME_SIZE + 2, column=4,
                                 sticky=W, columnspan=8)

        self.__radius_button = Button(background="green", relief=RAISED,
                                      borderwidth=5, text="Enter radius",
                                      command=self.radius)
        self.__radius_button.grid(row=GAME_SIZE + 2, column=10,
                                  columnspan=6)

        # color changing stuff
        # makes empty lists because all 3 entry lines are practically same
        self.__color_info = []
        self.__color_entry = []
        # makes the color labels and entries
        for n in ["R", "G", "B"]:
            self.__color_entry.append(Entry(background="white",
                                            borderwidth=5, text=f"{n}:"))
            self.__color_info.append(Label(text=f"{n} 0-255:"))

        # puts color labels and entries in grid
        i = 0
        for entry in self.__color_entry:
            entry.grid(row=GAME_SIZE + 3 + i, column=4,
                       sticky=W, columnspan=8)
            i += 1
        i = 0
        for label in self.__color_info:
            label.grid(row=GAME_SIZE + 3 + i, column=1,
                       sticky=W, columnspan=8)
            i += 1

        # color change activation button
        self.__color_button = Button(background="green", relief=RAISED,
                                     borderwidth=5, text="Enter color",
                                     command=self.color)
        self.__color_button.grid(row=GAME_SIZE + 7 + i, column=4,
                                 sticky=W, columnspan=8)

        # useful values stored
        # current color
        self.__color = (0, 0, 0)
        # coordinate data
        self.__coordinates = Coordinates()
        # current radius
        self.__radius = 5

        # refreshes the screen
        self.refresh_screen()

        self.__mainw.mainloop()

    def refresh_screen(self):

        y = 0

        while y < len(self.__coordinates.get_coordinates()):
            x = 0
            while x < len(self.__coordinates.get_coordinates()[y]):

                if self.__coordinates.get_coordinates()[y][x] == 1:
                    self.__game_field[y][x].configure(
                        background=rgb_color(self.__color))
                else:
                    self.__game_field[y][x].configure(background="#EEEEEE")

                x += 1
            y += 1

    def click(self, x, y):
        """
        does this when clicked
        :param x: int, x coordinate
        :param y: int, y coordinate
        :return:
        """
        # makes a circle
        self.__coordinates.circle((x, y), self.__radius)
        # updates the screen
        self.refresh_screen()

    def color(self):
        """
        Saves color to self.__color if input is correct
        :return:
        """
        rgb = []

        # put rgb values in a list
        for value in self.__color_entry:
            rgb.append(value.get())

        # tests if inputs are integers
        try:
            for i in range(len(rgb)):
                rgb[i] = int(rgb[i])
        except ValueError:
            return None

        # tests if inputs are 0-255
        for value in rgb:
            if not 0 <= value <= 255:
                return None

        # if we got here everything is good
        self.__color = (rgb[0], rgb[1], rgb[2])

        # updates the screen
        self.refresh_screen()

    def radius(self):
        """
        sets new radius from user entry
        :return:
        """
        radius = self.__radius_entry.get()

        # test if it is a float
        try:
            radius = int(radius)
        except ValueError:
            return None

        # test if the radius is negative or 0
        if radius <= 0:
            return None

        # if we got here everything is good
        self.__radius = radius

    def reset(self):
        """
        Calls the reset method
        :return:
        """
        self.__coordinates.reset()

        # updates the screen
        self.refresh_screen()

    def stop(self):

        self.__mainw.destroy()


def get_distance(point_1, point_2):
    """
    Calculates the distance between two points in a 2d space
    :param point_1: tuple int, point x and y
    :param point_2: tuplt int, point x and y
    :return: float, distance between the two
    """

    # store values
    x_1, y_1 = point_1
    x_2, y_2 = point_2

    # make a vector with two components
    vector_x = x_1 - x_2
    vector_y = y_1 - y_2

    # calculates the distance
    return math.sqrt(pow(vector_x, 2) + pow(vector_y, 2))


def rgb_color(rgb):
    """
    Converts rgb colors to hex
    :param rgb: (int, int, int)
    :return: string, hex value
    """
    return '#%02x%02x%02x' % rgb


def main():
    Userinterface()


if __name__ == '__main__':
    main()
