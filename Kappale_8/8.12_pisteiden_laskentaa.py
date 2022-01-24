"""
Pisteiden laskentaa
Eppu Hassinen
50044786
"""


def main():
    file_name = input("Enter the name of the score file: ")

    try:
        file = open(file_name, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return None

    scores = {}

    for line in file:
        line = line.rstrip()

        try:
            name, score = line.split()
        except ValueError:
            print("There was an erroneous line in the file:")
            print(line)
            return None

        try:
            if name not in scores:
                scores[name] = int(score)
            else:
                scores[name] += int(score)

        except ValueError:
            print("There was an erroneous score in the file:")
            print(score)
            return None

    print("Contestant score:")
    for i in sorted(scores.keys()):
        print(f"{i} {scores[i]}")

    file.close()


if __name__ == '__main__':
    main()
