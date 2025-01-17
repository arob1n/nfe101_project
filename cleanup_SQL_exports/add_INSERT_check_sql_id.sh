#!/bin/bash

# Check if a file name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide a file name."
    exit 1
fi

#
# Must clean generated file from openrefine export to SQL:
# ","  => ";"
# ( "  => ("
# " ), => ");
#


output_file="999_INSERT_table_join.sql"

#insert_line="INSERT INTO DiplomesValidateur VALUES"
#insert_line="INSERT INTO DiplomesCertificateur VALUES"
insert_line="INSERT INTO DiplomesCodeIdeo2 VALUES "

echo "" > $output_file

# for 1 line usage
#echo "INSERT INTO DiplomesValidateur VALUES " > $output_file
#echo "INSERT INTO DiplomesCertificateur VALUES " > $output_file
#echo "INSERT INTO DiplomesCodeIdeo2 VALUES " > $output_file



# Read the data file line by line
while IFS= read -r line; do
    # Change (" to "
    line_cleaned=$(echo $line | sed -e 's/("/"/g' | sed -e 's/");/"/g')
    #echo $line_cleaned
    # Split the line by ;
    IFS=';' read -r -a array <<< $line_cleaned
    
      # First element is the ID
      id=${array[0]}

      # Loop through the remaining elements
      # It automatically ignore ID without values
      for ((i=1; i<${#array[@]}; i++)); do
          name_to_find_raw=${array[i]}
	  # Change double singlequote, to single singlequote, as it's blocking for INSERT, not for SELECT
          name_to_find=$(echo $name_to_find_raw | sed -e "s/''/'/g")

          # Generate the SQL insert statement
          #echo "$insert_line ($id, (SELECT id FROM Validateurs WHERE Validateur = $name_to_find));" >> $output_file
	  #echo "$insert_line ($id, (SELECT id FROM Certificateurs WHERE Certificateur = $name_to_find));" >> $output_file
	  echo "$insert_line ($id, (SELECT id FROM CodeIdeo2 WHERE CodeIdeo2 = $name_to_find));" >> $output_file
      done


done < "$1"

# Output message
echo "Completed"
