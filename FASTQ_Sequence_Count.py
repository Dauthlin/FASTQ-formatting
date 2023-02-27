# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Bio import SeqIO

def Sequence(path):
    total = 0
    with open(path) as file:
        for line in file:
            if line.rstrip() == "":
                total += 1
    return total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "Testing/fake_test_file"
    print(Sequence(path))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
