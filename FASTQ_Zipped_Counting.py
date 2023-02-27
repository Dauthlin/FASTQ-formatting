
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Bio import SeqIO
import gzip
from mimetypes import guess_type
from functools import partial

def Sequence(file):
    total = 0
    for line in file:
        if line.rstrip() == "":
            total += 1
    return total


def Nucleotide(file):
    total = 0
    # checks what encoding type it is using

    # if its gzip then
    for record in SeqIO.parse(file, "fastq"):
        total += len(record.seq)
    return total

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "Testing/fake_test_file.fastq.gz"
    # using information from https://stackoverflow.com/questions/42757283/seqio-parse-on-a-fasta-gz
    encoding = guess_type(path)[1]  # uses file extension
    _open = partial(gzip.open, mode='rt') if encoding == 'gzip' else open
    with _open(path) as file:
        print(Nucleotide(file))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
