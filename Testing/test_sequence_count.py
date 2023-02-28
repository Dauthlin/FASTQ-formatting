import os
import subprocess

def run(cmd):
    # print(cmd)
    try:
        completed = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    return completed


def test_file_and_series_with_blanks():
    # gets the path of the program to test
    program_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "FASTQ_Sequence_Count.py")
    # gets the path of the data
    data_path = os.path.join(os.path.dirname(__file__), "fake_test_file_with_blank_lines.fastq")
    # combines them into a single command
    command = str("python " + program_path + " -f " + data_path + " -s true")
    # runs the command
    result = (run(cmd=command)).decode('ascii').strip()
    assert result == "1.75"

def test_file_and_series_no_blanks():
    # gets the path of the program to test
    program_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "FASTQ_Sequence_Count.py")
    # gets the path of the data
    data_path = os.path.join(os.path.dirname(__file__), "fake_test_file.fastq")
    # combines them into a single command
    command = str("python " + program_path + " -f " + data_path + " -s true")
    # runs the command
    result = (run(cmd=command)).decode('ascii').strip()
    assert result == "0.0"


if __name__ == '__main__':
    # debugging area
    program_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "FASTQ_Sequence_Count.py")
    data_path = os.path.join(os.path.dirname(__file__), "fake_test_file_with_blank_lines.fastq")
    command = str("python " + program_path + " -f " + data_path + " -s true")
    result = (run(cmd=command)).decode('ascii').strip()
    #
    print(result)
