"""
Program reads a csv file and makes a data structure data[name][key]
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def read_file(file_name):
    """
    Stores the values from a csv file to a dict
    :param file_name: Name of the CSV file
    :return: Dict formatted data[name_key][data_key] = data
    """
    try:
        file = open(file_name, mode="r")
    except OSError:
        print(f"There was an error opening the file: {file_name}")
        return None
    # for checking the headers in the file
    header = True
    # keys are the header names
    keys = []
    # store the dict to returning
    data = {}

    # goes through the file line by line
    for line in file:

        # saves header names in a List
        if header:
            for key in line.strip().split(";"):
                keys.append(key)
                header = False

        # stores the values from each line in to a dictionary
        else:
            # to store the dict
            facts = {}
            # makes the line in to a list
            line_data = line.strip().split(";")
            # goes through each lines data
            for i in range(1, len(keys)):
                facts[keys[i]] = line_data[i]
            data[line_data[0]] = facts

    return data


def main():
    pass


if __name__ == '__main__':
    main()
