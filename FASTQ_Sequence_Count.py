import argparse
def Sequence(path):
    total = 0
    with open(path) as file:
        for line in file:
            if line.rstrip() == "":
                total += 1
    return total / 4


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="File Name")
    parser.add_argument("-s", "--sequence", help="Count sequences")
    args = parser.parse_args()
    if args.sequence is not None:
        print(Sequence(args.filename))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
