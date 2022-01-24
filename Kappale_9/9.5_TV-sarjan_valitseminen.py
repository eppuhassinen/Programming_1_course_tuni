"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""


def read_file(filename):

    """
    Reads and saves the series and their genres from the file.
    :param filename: txt file where every line is "Movie;genre,genre,genre..."
    :return Dict with lists. Genres and lists are movies tagged with that
    genre.
    """

    # TODO initialize a new data structure
    genre_data = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            # TODO add the name and genres data to the data structure
            for i in genres:
                if i not in genre_data:
                    genre_data[i] = []
                genre_data[i].append(name)

        file.close()
        # TODO return the data structure
        return genre_data

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    # TODO print the genres
    genres_print = "Available genres are: "
    for key in sorted(genre_data.keys()):
        genres_print += f"{key}, "

    print(genres_print.rstrip(", "))

    while True:
        genre = input("> ")

        if genre == "exit":
            return
        if genre not in genre_data:
            continue
        # TODO print the series belonging to a genre.
        for i in sorted(genre_data[genre]):
            print(i)


if __name__ == "__main__":
    main()
