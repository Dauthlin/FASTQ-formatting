# FASTQ-formatting

To run the program select which version of the script you would like to run. 
FASTQ_Sequence_Count.py only covers user case 1 
FASTQ_Nucleotides_Count.py covers user case 1 and 2
FASTQ_Zipped_Counting.py covers user case 1, 2 and 3

To run the program in your command line type:
  python PROGRAM_VERSION_HERE.py 
 
Depending on which version you are using you will have access to up to 3 flags.

in FASTQ_Sequence_Count.py you have -f which selects the filename and -s True which selects whether you would like to perform a sequence count.

in FASTQ_Nucleotides_Count.py and FASTQ_Zipped_Counting.py you have access to both above flags as well as -n True which allows you to select if you would like to do a nucleotide count.

To create new tests please do so in the Testing folder using pytest. These tests will be run automatically on new pushes to the repository 

Add new requirements to the requirements.txt file
