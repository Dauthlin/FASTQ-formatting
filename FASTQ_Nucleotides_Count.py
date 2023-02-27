import argparse
from Bio import SeqIO

def Sequence(path):
    total = 0
    with open(path) as file:
        for line in file:
            if line.rstrip() == "":
                total += 1
    return total / 4

def Nucleotide(path):
    total = 0
    for record in SeqIO.parse(path, "fastq"):
        total += len(record.seq)
    return total

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="File Name")
    parser.add_argument("-s", "--sequence", help="Count sequences")
    parser.add_argument("-n", "--nucleotide", help="Count nucleotides")
    args = parser.parse_args()
    if args.nucleotide is not None:
        print(Nucleotide(args.filename))
    if args.sequence is not None:
        print(Sequence(args.filename))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
