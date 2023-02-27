
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

def Nucleotide(path):
    total = 0
    for record in SeqIO.parse(path, "fastq"):
        total += len(record.seq)
    return total

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "Testing/fake_test_file.fastq"
    print(Nucleotide(path))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
