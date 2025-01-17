#!/bin/bash


# Check if a file name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Give me a file"
    exit 1
fi

# needs to be in format ("xxx");


# Output data file
output_file="transformed_data.sql"

echo "INSERT INTO VALUES" > $output_file

# Initialize ID
id=1

# Read the input file line by line
while IFS= read -r line; do

    line=$(echo $line | sed -e 's/("//g' | sed -e 's/");//g')
    # Add ID 
    new_line="(\"$id\",\"$line\"),"

    echo $new_line >> $output_file

    # Increment ID
    id=$((id+1))
done < "$1"
