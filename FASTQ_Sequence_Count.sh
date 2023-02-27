#!/bin/bash

# debugging test files
#file="Testing/1_control_ITS2_2019_minq7.fastq"
#file2="Testing/fake_test_file"

# total stores the number of lines that do not start with 0 or more white spaces then end
total=$(grep -cvP '^\s*$' $1)
echo $((total / 4))
#read -p "Press any key to continue "