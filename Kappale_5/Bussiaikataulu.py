"""
Bussiaikataulu
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def find_next_bus(t, bus_times):
    """
    Finds the next bus departure time
    :param t: int, time
    :param bus_times: list, bus times
    :return: int, index of the next bus time in the list
    """

    i = 0

    for i in range(len(bus_times)):
        if t <= bus_times[i]:
            return i
    return 0


def next_3_buses(first_bus, bus_times):
    """
    Returns a list of next three bus times
    :param first_bus: int, index of the first one
    :param bus_times: list, bus times
    :return: list, of 3 bus times
    """
    next_buses = []

    i = 0
    n = first_bus
    while i < 3:
        if n < len(bus_times) - 1:
            next_buses.append(bus_times[n])
            n += 1
        else:
            next_buses.append(bus_times[n])
            n = 0

        i += 1

    return next_buses


def main():
    # "630" is 06:30, "1015" is 10:15 etc.
    bus_times = [630, 1015, 1415, 1620, 1720, 2000]

    current_time = int(input("Enter the time (as an integer): "))

    # finds the next leaving bus with current time
    next_bus = find_next_bus(current_time, bus_times)

    # print next 3 bus departure times
    print("The next buses leave:")
    for n in next_3_buses(next_bus, bus_times):
        print(n)


if __name__ == '__main__':
    main()
