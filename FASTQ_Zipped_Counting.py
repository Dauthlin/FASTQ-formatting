
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Bio import SeqIO
import gzip
from mimetypes import guess_type
from functools import partial
import argparse

def Sequence(file):
    total = 0
    for line in file:
        if line.rstrip() == "":
            total += 1
    return total / 4


def Nucleotide(file):
    total = 0
    # only loop through the sequences
    for record in SeqIO.parse(file, "fastq"):
        total += len(record.seq)
    return total

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="File Name")
    parser.add_argument("-s", "--sequence", help="Count sequences")
    parser.add_argument("-n", "--nucleotide", help="Count nucleotides")
    args = parser.parse_args()
    # using information from https://stackoverflow.com/questions/42757283/seqio-parse-on-a-fasta-gz
    # checks what encoding type it is using
    encoding = guess_type(args.filename)[1]  # uses file extension
    # creates a partial function if the encoding type is gzip
    _open = partial(gzip.open, mode='rt') if encoding == 'gzip' else open
    with _open(args.filename) as file:
        if args.nucleotide is not None:
            print(Nucleotide(file))
        if args.sequence is not None:
            print(Sequence(file))



