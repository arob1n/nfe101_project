# Instruction to install this project

Only tested and running on Linux ubuntu >= 22.04

Data to use:
https://www.data.gouv.fr/fr/datasets/referentiel-national-des-certifications/#/resources/f2981d6f-e55c-42cd-8eba-3e891777e222

If you cannot access it, the data is present in `./DATA/000_opendata-certifinfo-01012025.csv`

The instruction suppose you already have your data refined via openrefine and your are using `;` to separate items inside the same column

## Install locally

### Ubuntu

Be inside this repository
```
cd [my-project] 
```

#### Install python
Install python3:
```
sudo apt update
sudo apt install python3.10
```

Install pip3:
```
sudo apt update
sudo apt install python3-pip
sudo apt install python3-virtualenv
```

##### Work in a Virtual-env 
Go into the project folder and activate venv:
```
virtualenv env
source env/bin/activate
```

Install the prerequirements:
```
pip3 install -r requirements.txt
```

#### Install mariadb

```
sudo apt update
sudo apt install mariadb-server
```

Launch the secure script to disable root login from remote
```
sudo mysql_secure_installation
```

Create the Database nfe_101
```
sudo mariadb
CREATE DATABASE nfe_101;
exit
```

Create the tables
NOTE: you have to create tables via the SQL script as python do not manage INT UNSIGNED (negative integer for CodeDiplome)
```
sudo mariadb
USE nfe_101;
SOURCE ./SQL_scripts/001_CREATE_tables.sql;
exit
```

##### (optional) Fill the tables with data

Fill the tables
Otherwise, export/import the CSV file as explained further in the doc
```
sudo mariadb
USE nfe_101;
SOURCE ./SQL_scripts/010_INSERT_Diplomes_full.sql;
SOURCE ./SQL_scripts/101_INSERT_list_validateur.sql;
SOURCE ./SQL_scripts/201_INSERT_list_certificateur.sql;
SOURCE ./SQL_scripts/301_INSERT_list_codeid02.sql;
SOURCE ./SQL_scripts/102_ID_diplome_to_validateur.sql;
SOURCE ./SQL_scripts/202_ID_diplome_to_certificateur.sql;
SOURCE ./SQL_scripts/302_ID_diplome_to_codeid02.sql;
exit
```

Create user for our application
NOTE: As this user needs CRUD access, we need to update his permission
```
sudo mariadb
CREATE USER 'DBU_NFE101'@'localhost' IDENTIFIED BY 'CeciEstUnProtoNFE101';
FLUSH PRIVILEGES;
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON nfe_101.* TO 'DBU_NFE101'@'localhost';
FLUSH PRIVILEGES;
exit
```

If you want to verify the user roles:
```
sudo mariadb
SHOW GRANTS FOR 'DBU_NFE101'@localhost;
exit
```


##### Optionnal: Delete the tables
Only if you want to delete the tables !

Respect the order for FOREIGN_KEY relationship

```
sudo mariadb
USE nfe_101;
DROP TABLE DiplomesCertificateur;
DROP TABLE DiplomesValidateur;
DROP TABLE DiplomesCodeIdeo2;
DROP TABLE CodeIdeo2;
DROP TABLE Validateurs;
DROP TABLE Certificateurs;
DROP TABLE Diplomes;
```

##### Optionnal: Install adminer for a simple DB exploration

```
sudo apt update
sudo apt install adminer
sudo a2enconf adminer
sudo systemctl reload apache2
```

Now you can access it via:

http://localhost/adminer/?server=localhost

System: Mysql
Server: localhost
Username: DBU_NFE101
Password: CeciEstUnProtoNFE101
Database: nfe_101



#### Kafka

##### Install Kafka

Get the version from
https://kafka.apache.org/quickstart

```
cd NFE101_PROJECT
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
```
And the SHA512 file
```
cd NFE101_PROJECT
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz.sha512
```

[!NOTE] 
Verify the SHA512 file follow the convention "SHA512 filename", without any spaces for the key

Compare both file:

```
cd NFE101_PROJECT
sha512sum --check kafka_2.13-3.9.0.tgz.sha512
```

If everything is OK, we can untar it into kafka-server:
```
tar -xzf kafka_2.13-3.9.0.tgz --one-top-level=kafka-server
```

Configure Kafka
```
KAFKA_CLUSTER_ID="$(kafka-server/kafka_2.13-3.9.0/bin/kafka-storage.sh random-uuid)"
kafka-server/kafka_2.13-3.9.0/bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c kafka-server/kafka_2.13-3.9.0/config/kraft/reconfig-server.properties
```

Launch kafka
```
kafka-server/kafka_2.13-3.9.0/bin/kafka-server-start.sh kafka-server/kafka_2.13-3.9.0/config/kraft/reconfig-server.properties
```


##### Manage Kafka

If you want to manage Kafka, you can use the built-in commands, or kafkactl (which is simplier, and faster)
https://github.com/deviceinsight/kafkactl

We get the binary file directly (not recommanded for production use, for a local dev usage, it's acceptable):
```
cd NFE101_PROJECT
wget https://github.com/deviceinsight/kafkactl/releases/download/v5.4.0/kafkactl_5.4.0_linux_amd64.tar.gz
tar -xvf kafkactl_5.4.0_linux_amd64.tar.gz -C kafka-server
```

Documentation kafkactl:
https://deviceinsight.github.io/kafkactl/

Get the brokers info:
NOTE: The .kafkactl_config is already included in this project
```
kafka-server/kafkactl get brokers -C .kafkactl_config
```

##### Create topic, user and consummer-group

Create topic
```
kafka-server/kafkactl create topic streams-input-diplomes -C .kafkactl_config
kafka-server/kafkactl create topic Diplomes -C .kafkactl_config
kafka-server/kafkactl create topic Validateur -C .kafkactl_config
kafka-server/kafkactl create topic Link_Validateur -C .kafkactl_config
kafka-server/kafkactl create topic Certificateurs -C .kafkactl_config
kafka-server/kafkactl create topic Link_Certificateur -C .kafkactl_config
kafka-server/kafkactl create topic CodeIdeo2 -C .kafkactl_config
kafka-server/kafkactl create topic Link_CodeIdeo2 -C .kafkactl_config
```


Create ConsumerGroup
Set it to the oldest, so if we start producing before the creation, we do not miss a message
```
kafka-server/kafkactl create consumer-group CG-Diplomes --topic Certificateurs --topic CodeIdeo2 --topic Diplomes --topic Link_Certificateur --topic Link_CodeIdeo2 --topic Link_Validateur --topic Validateur -C .kafkactl_config --oldest
```

##### Check kafka values

```
kafka-server/kafkactl describe topic streams-input-diplomes -C .kafkactl_config

kafka-server/kafkactl describe consumer-group CG-Diplomes -C .kafkactl_config
```

##### Reset offset (if needed)

```
kafka-server/kafkactl reset offset CG-Diplomes --topic Diplomes --oldest -C .kafkactl_config --execute
```

#### Export Openrefine data

As of now, split message / integration / kafka stream is not ready

So we have to export the openrefine data in a specific way

##### Option 1: as CSV


If you export as "comma separated values", it automatically generates a complete CSV export
The objective is to only send the CSV, and a kakfa stream will split it into different topic

Save the file in this project under `./DATA/900_full_no_filter_diplomes.csv`




##### Option 2: as SQL

We need 6 different exports, they are already available in `./DATA/` you can skip this

###### Export Diplomes

Open the project with all data cleaned

*Export > SQL...*

Unselect "validateur" + "certificateur" + "CodeIdeo2"

Enable only these parameters:
- output empty row
- Trim colum name
- Include INSERT INTO command
  - Convert null value to NULL in INSERT

Download the file

Save it into this project in `./DATA/001_diplomes.sql`

###### Export Validateur name

For this, we need to do some cleanup:

In the column options for "valideur":
- Edit column
- Split into several columns
- By separator `;`
  - keep enabled the "guess cell type" and "remove this column"

In the column option for "valideur 1":
- Transpose
- Transpose cells accross columns into rows
  - From "valideur 1" to "valideur 97"
  - One column "one_vaalideur"
  - Ignore blanck cells
  - Fill down in other columns
  - click on "transpose"

In the column option for "one_valideur":
- Sort...
  - sort by text
  - order "a - z"
  - position: Valid values > Errors> Blanks
  - click on "OK"

Next to the number of row displayed, click on "Sort" > "Reorder rows permanently"

In the column option for "one_valideur":
- Edit cells
- Blank Down

In the column option for "one_valideur":
- Facet
- Customized facets
- Facet by blank (null or empty string)

On the left, the facet by blanck must be selected on "true"

In the column option for "All":
- Edit rows 
- Remove matching rows

Reset the blank facet by closing it

*Export > SQL...*

Unselect all options

Select only one_valideur

Enable only these parameters:
- output empty row
- Trim colum name
- Include INSERT INTO command
  - Convert null value to NULL in INSERT

Download the file

Save it into this project in `./DATA/011_valideur.sql`

Undo to the previous state before our actions

###### Export Diplome ID + Validateur name

For this, we need to do some cleanup:

In the column options for "valideur":
- Edit column
- Split into several columns
- By separator `;`
  - keep enabled the "guess cell type" and "remove this column"

In the column option for "valideur 1":
- Transpose
- Transpose cells accross columns into rows
  - From "valideur 1" to "valideur XX"
  - One column "one_valideur"
  - Ignore blanck cells
  - Fill down in other columns
  - click on "transpose"

In the column option for "one_valideur":
- Sort...
  - sort by text
  - order "a - z"
  - position: Valid values > Errors> Blanks
  - click on "OK"




*Export > SQL...*


Select only `Code_Diplome` and all the `valideur X` column


Enable only these parameters:
- output empty row
- Trim colum name
- Include INSERT INTO command

Download the file

[!IMPORTANT]
NOTE: If the server crash, do the export with "Convert null value to NULL in INSERT" and replace the null values after `sed -e "s/,null//g"` => in general, just restart refine and it should work

Save it into this project in `./DATA/012_diplomes_and_valideur.sql`

Undo to the previous state before our actions


###### Export Certificateurs name

For this, we need to do some cleanup:

In the column options for "certificateur":
- Edit column
- Split into several columns
- By separator `;`
  - keep enabled the "guess cell type" and "remove this column"

In the column option for "certificateur 1":
- Transpose
- Transpose cells accross columns into rows
  - From "certificateur 1" to "certificateur XX"
  - One column "one_certificateur"
  - Ignore blanck cells
  - Fill down in other columns
  - click on "transpose"

In the column option for "one_certificateur":
- Sort...
  - sort by text
  - order "a - z"
  - position: Valid values > Errors> Blanks
  - click on "OK"

Next to the number of row displayed, click on "Sort" > "Reorder rows permanently"

In the column option for "one_certificateur":
- Edit cells
- Blank Down

In the column option for "one_certificateur":
- Facet
- Customized facets
- Facet by blank (null or empty string)

On the left, the facet by blanck must be selected on "true"

In the column option for "All":
- Edit rows 
- Remove matching rows

Reset the blank facet by closing it

*Export > SQL...*

Unselect all options

Select only `one_certificateur`

Enable only these parameters:
- output empty row
- Trim colum name
- Include INSERT INTO command
  - Convert null value to NULL in INSERT

Download the file

Save it into this project in `./DATA/021_certificateur.sql`

Undo to the previous state before our actions

###### Export Diplome ID + Certificateurs name


For this, we need to do some cleanup:

In the column options for "certificateur":
- Edit column
- Split into several columns
- By separator `;`
  - keep enabled the "guess cell type" and "remove this column"



*Export > SQL...*


Select only `Code_Diplome` and all the `certificateur X` column


Enable only these parameters:
- output empty row
- Trim colum name
- Include INSERT INTO command

Download the file

Save it into this project in `./DATA/022_diplomes_and_certificateur.sql`

Undo to the previous state before our actions




###### Export CodeIdeo2 name

For this, we need to do some cleanup:

In the column options for "CodeIdeo2":
- Edit column
- Split into several columns
- By separator `;`
  - keep enabled the "guess cell type" and "remove this column"

In the column option for "CodeIdeo2 1":
- Transpose
- Transpose cells accross columns into rows
  - From "CodeIdeo2 1" to "CodeIdeo2 XX"
  - One column "one_codeideo2"
  - Ignore blanck cells
  - Fill down in other columns
  - click on "transpose"

In the column option for "one_codeideo2":
- Sort...
  - sort by text
  - order "a - z"
  - position: Valid values > Errors> Blanks
  - click on "OK"

Next to the number of row displayed, click on "Sort" > "Reorder rows permanently"

In the column option for "one_codeideo2":
- Edit cells
- Blank Down

In the column option for "one_codeideo2":
- Facet
- Customized facets
- Facet by blank (null or empty string)

On the left, the facet by blanck must be selected on "true"

In the column option for "All":
- Edit rows 
- Remove matching rows

Reset the blank facet by closing it

*Export > SQL...*

Unselect all options

Select only `one_codeideo2`

Enable only these parameters:
- output empty row
- Trim colum name
- Include INSERT INTO command
  - Convert null value to NULL in INSERT

Download the file

Save it into this project in `./DATA/031_codeideo2.sql`

Undo to the previous state before our actions

###### Export Diplome ID + CodeIdeo2 name


For this, we need to do some cleanup:

In the column options for "CodeIdeo2":
- Edit column
- Split into several columns
- By separator `;`
  - keep enabled the "guess cell type" and "remove this column"


*Export > SQL...*


Select only `Code_Diplome` and all the `CodeIdeo2 X` column


Enable only these parameters:
- output empty row
- Trim colum name
- Include INSERT INTO command
  - Convert null value to NULL in INSERT

Download the file

Save it into this project in `./DATA/032_diplomes_and_codeideo2.sql`

Undo to the previous state before our actions

###### Cleanup the files

Change the first line of each file to match the table to insert

Using the scripts in `./cleanup_SQL_exports/` if they are needed (add id, add insert "where")

add_id_to_each_line_sql_insert.sh file.sql

The cleaned file are already available in `./SQL_scripts`


#### Import Openrefine data

##### Option 1: import the CSV



Launch the kafka stream filter before importing the CSV

```
python3 kafka-scripts/filter_stream_in_all_topics.py worker
```

In a new terminal, import the CSV into kafka topic `streams-input-diplomes`

[!IMPORTANT]
You must remove the first line of the generated CSV (with the column header name) as the import is not dynamic.
Once done, change the name from `900_full_no_filter_diplomes.csv` to `999_ready_to_import.csv`

```
python3 kafka-scripts/insert_csv_to_kafka.py ./DATA/999_ready_to_import.csv streams-input-diplomes
```


Launch the kafka insertion script

```
python3 kafka-scripts/read_topics_and_insert_in_db.py
```

##### Option 2: import the SQL files

See instructions "Fill the tables with data" 


#### Launch the API server

To access to API, use (make sure you are in the venv):
```
uvicorn main:app --reload
```

##### graphical acces

A graphical interface for the API is available here (once the server is launched):
http://127.0.0.1:8000/docs