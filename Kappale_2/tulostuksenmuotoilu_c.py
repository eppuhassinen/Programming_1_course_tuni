"""
Tehtävä välilyönnit kuntoon
Eppu Hassinen
Student number: 50044786
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i * j:4}', end="")
        print()


if __name__ == "__main__":
    main()
