# project repository for nfe_101 2024/25

## Installation

See instructions.md


## Objective

Get data from OpenData - OK

Refine it via OpenRefine - OK

Export the data to a CSV/SQL file - OK

Import the generated file and send it to kafka, 1 line at a time - OK

Using kafka stream break the file into multiple topics - OK

Connect to kafka topic and inject the data in a database - OK

Expose the data in the database via a CRUD API - OK


## Missing

1.API self-reference for FastAPI

2.API complete cross data (left-join) (get ID and it respond the whole list, you can do it via SQL)
```sql
SELECT 
Diplomes.Libelle_Diplome AS Diplome_Name,
Diplomes.Code_Diplome,
DiplomesCertificateur.id_certificateur,
Certificateurs.Certificateur AS Certificateur_Name,
DiplomesValidateur.id_validateur,
Validateurs.Validateur AS Validateur_Name,
CodeIdeo2.id,
CodeIdeo2.CodeIdeo2 AS CodeIdeo2
FROM 
Diplomes
LEFT JOIN 
DiplomesCertificateur ON Diplomes.Code_Diplome = DiplomesCertificateur.id_diplome
LEFT JOIN 
Certificateurs ON DiplomesCertificateur.id_certificateur = Certificateurs.id
LEFT JOIN
DiplomesValidateur ON Diplomes.Code_Diplome = DiplomesValidateur.id_diplome
LEFT JOIN
Validateurs ON DiplomesValidateur.id_validateur = Validateurs.id
LEFT JOIN
DiplomesCodeIdeo2 ON Diplomes.Code_Diplome = DiplomesCodeIdeo2.id_diplome
LEFT JOIN
CodeIdeo2 ON DiplomesCodeIdeo2.id_ideo = CodeIdeo2.CodeIdeo2 

WHERE
Diplomes.Code_Diplome = 12362;
```

3.API possibility to delete 1 diplome automatically (Cascade mode)

4.UnitTest