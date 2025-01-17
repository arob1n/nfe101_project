#!/bin/bash
#workaround script as the SQL export crash (error 500... java null pointer exception) 


# Check if a file name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide a file name."
    exit 1
fi

output_file=./cleaned_file.sql


# Read the data file line by line
while IFS= read -r line; do
	# Add missing start of line + end of line
	line_cleaned=$(echo $line | sed -e 's/^/("/g' | sed -e 's/$/");/g') 
        echo $line_cleaned >> $output_file
done < "$1"

