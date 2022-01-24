"""
Tiedoston nimien numerointi
Eppu Hassinen
50044786
"""


def main():
    file_name = input("Enter the name of the file: ")

    file = open(file_name, mode="r")

    # stores the line number
    i = 1

    for file_line in file:
        print(f"{i} {file_line.rstrip()}")
        i += 1

    file.close()


if __name__ == '__main__':
    main()
