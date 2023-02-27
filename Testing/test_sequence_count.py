import os
from subprocess import check_output

def test_initialize():
    assert True == True


# this block works but only on windows
# def run(cmd):
#     completed = check_output(["powershell", "-Command", cmd])
#     return completed
#
#
# def test_file_and_series():
#     # gets the path of the program to test
#     data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "FASTQ_Sequence_Count.py")
#     # runs the program on the copmmand line
#     result = (run(cmd="python " + data_path + " -f fake_test_file_with_blank_lines.fastq -s true")).decode('ascii').strip()
#     assert str(result) == "1.75"
#
#
# if __name__ == '__main__':
#     data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "FASTQ_Sequence_Count.py")
#     result = (run(cmd="python " + data_path + " -f fake_test_file_with_blank_lines.fastq")).decode('ascii').strip()
#     print(result)
