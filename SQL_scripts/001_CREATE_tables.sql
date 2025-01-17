-- Liste des diplomes
CREATE TABLE Diplomes (
    Code_Diplome INT UNSIGNED PRIMARY KEY,
    Libelle_Diplome VARCHAR(255) NOT NULL,
    Libelle_Type_Diplome VARCHAR(255) NOT NULL,
    Code_Niveau_Europeen INT UNSIGNED,
    Date_MaJ DATE,
    Code_FormaCode INT UNSIGNED,
    Libelle_FormaCode VARCHAR(255),
    Code_Rome_1 VARCHAR(5),
    Code_Rome_2 VARCHAR(5),
    Code_Rome_3 VARCHAR(5),
    Code_Rome_4 VARCHAR(5),
    Code_Rome_5 VARCHAR(5),
    Code_Nsf INT UNSIGNED,
    Code_RNCP INT UNSIGNED,
    Code_RS INT UNSIGNED,
    Code_Scolarite VARCHAR(255),
    Annee_Premiere_Session INT UNSIGNED,
    Annee_Derniere_Session INT UNSIGNED,
    Code_Ancien_Diplome INT UNSIGNED,
    Intitule_Ancien_Diplome VARCHAR(255),
    Code_Ancien_RNCP INT UNSIGNED,
    Code_Ancien_Scolarite VARCHAR(8),
    Etat INT UNSIGNED,
    Etat_Libelle VARCHAR(100),
    Etat_Ancien_Diplome INT UNSIGNED,
    Etat_Ancien_Diplome_Libelle VARCHAR(100),
    Accessibilite_fi INT UNSIGNED,
    Accessibilite_ca INT UNSIGNED,
    Accessibilite_fc INT UNSIGNED,
    Accessibilite_cp INT UNSIGNED,
    Accessibilite_vae INT UNSIGNED,
    Accessibilite_ind INT UNSIGNED,
    Code_type_diplome INT UNSIGNED
);

-- Liste des validateur
CREATE TABLE Validateurs (
    id INT UNSIGNED PRIMARY KEY,
    Validateur VARCHAR(255) NOT NULL
);

-- JOIN validateur et diplome
CREATE TABLE DiplomesValidateur (
    id_diplome INT UNSIGNED,
    id_validateur INT UNSIGNED,
    PRIMARY KEY (id_diplome, id_validateur),
    FOREIGN KEY (id_diplome) REFERENCES Diplomes(Code_Diplome) ON DELETE CASCADE,
    FOREIGN KEY (id_validateur) REFERENCES Validateurs(id) ON DELETE CASCADE
);


-- Liste des Certificateurs
CREATE TABLE Certificateurs (
    id INT UNSIGNED PRIMARY KEY,
    Certificateur VARCHAR(255) NOT NULL
);

-- JOIN certificateur et diplome
CREATE TABLE DiplomesCertificateur (
    id_diplome INT UNSIGNED,
    id_certificateur INT UNSIGNED,
    PRIMARY KEY (id_diplome, id_certificateur),
    FOREIGN KEY (id_diplome) REFERENCES Diplomes(Code_Diplome) ON DELETE CASCADE,
    FOREIGN KEY (id_certificateur) REFERENCES Certificateurs(id) ON DELETE CASCADE
);

-- Liste CodeIdeo2
CREATE TABLE CodeIdeo2 (
    id INT UNSIGNED PRIMARY KEY,
    CodeIdeo2 VARCHAR(15) NOT NULL
);


-- JOIN CodeIdeo2
CREATE TABLE DiplomesCodeIdeo2 (
    id_diplome INT UNSIGNED,
    id_ideo INT UNSIGNED,
    PRIMARY KEY (id_diplome, id_ideo),
    FOREIGN KEY (id_diplome) REFERENCES Diplomes(Code_Diplome) ON DELETE CASCADE,
    FOREIGN KEY (id_ideo) REFERENCES CodeIdeo2(id) ON DELETE CASCADE
);
