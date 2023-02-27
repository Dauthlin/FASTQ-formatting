#!/bin/bash
file="Testing/1_control_ITS2_2019_minq7.fastq"
file2="Testing/fake_test_file"
grep -cvP '^\s*$' $file

read -p "Press any key to continue "