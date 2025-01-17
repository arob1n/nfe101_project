# Easier to read with Optional
from typing import Optional
# For date format
from datetime import date
# Used for data validation
from pydantic import BaseModel

# for kafka validation model
import faust

# define Class, as request models, and validation of input data
class FullDiplome(BaseModel):
    """
    Mandatory fields:
    Code_Diplome
    Libelle_Diplome
    Libelle_Type_Diplome
    """
    Code_Diplome: int
    Libelle_Diplome: str
    Libelle_Type_Diplome: str
    Code_Niveau_Europeen: Optional[int]
    Date_MaJ: Optional[date]
    Code_FormaCode: Optional[int]
    Libelle_FormaCode: Optional[str]
    Code_Rome_1: Optional[str]
    Code_Rome_2: Optional[str]
    Code_Rome_3: Optional[str]
    Code_Rome_4: Optional[str]
    Code_Rome_5: Optional[str]
    Code_Nsf: Optional[int]
    Code_RNCP: Optional[int]
    Code_RS: Optional[int]
    Code_Scolarite: Optional[str]
    Annee_Premiere_Session: Optional[int]
    Annee_Derniere_Session: Optional[int]
    Code_Ancien_Diplome: Optional[int]
    Intitule_Ancien_Diplome: Optional[str]
    Code_Ancien_RNCP: Optional[int]
    Code_Ancien_Scolarite: Optional[str]
    Etat: Optional[int]
    Etat_Libelle: Optional[str]
    Etat_Ancien_Diplome: Optional[int]
    Etat_Ancien_Diplome_Libelle: Optional[str]
    Accessibilite_fi: Optional[int]
    Accessibilite_ca: Optional[int]
    Accessibilite_fc: Optional[int]
    Accessibilite_cp: Optional[int]
    Accessibilite_vae: Optional[int]
    Accessibilite_ind: Optional[int]
    Code_type_diplome: Optional[int]


class FullValidateur(BaseModel):
    id: int
    Validateur: str

class FullDiplomeValidateur(BaseModel):
    id_diplome: int
    id_validateur: int

class FullCertificateur(BaseModel):
    id: int
    Certificateur: str

class FullDiplomeCertificateur(BaseModel):
    id_diplome: int
    id_certificateur: int

class FullCodeIdeo2(BaseModel):
    id: int
    CodeIdeo2: str

class FullDiplomeCodeIdeo2(BaseModel):
    id_diplome: int
    id_ideo: int




##########################################################

# define Class, as request models, and validation of input data
class CFullDiplome(faust.Record):
    """
    Mandatory fields, as in DB:
    Code_Diplome => ID
    Libelle_Diplome => Name
    Libelle_Type_Diplome => Type
    """
    Code_Diplome: int
    Libelle_Diplome: str
    Libelle_Type_Diplome: str
    Code_Niveau_Europeen: Optional[int]
    Date_MaJ: Optional[date]
    Code_FormaCode: Optional[int]
    Libelle_FormaCode: Optional[str]
    Code_Rome_1: Optional[str]
    Code_Rome_2: Optional[str]
    Code_Rome_3: Optional[str]
    Code_Rome_4: Optional[str]
    Code_Rome_5: Optional[str]
    Code_Nsf: Optional[int]
    Code_RNCP: Optional[int]
    Code_RS: Optional[int]
    Code_Scolarite: Optional[str]
    Annee_Premiere_Session: Optional[int]
    Annee_Derniere_Session: Optional[int]
    Code_Ancien_Diplome: Optional[int]
    Intitule_Ancien_Diplome: Optional[str]
    Code_Ancien_RNCP: Optional[int]
    Code_Ancien_Scolarite: Optional[str]
    Etat: Optional[int]
    Etat_Libelle: Optional[str]
    Etat_Ancien_Diplome: Optional[int]
    Etat_Ancien_Diplome_Libelle: Optional[str]
    Accessibilite_fi: Optional[int]
    Accessibilite_ca: Optional[int]
    Accessibilite_fc: Optional[int]
    Accessibilite_cp: Optional[int]
    Accessibilite_vae: Optional[int]
    Accessibilite_ind: Optional[int]
    Code_type_diplome: Optional[int]

class CFullValidateur(faust.Record):
    Validateur: str
    # as we do not know yet the validateur ID
    # id_validateur

class CDiplomeValidateur(faust.Record):
    id_diplome: int
    Validateur: str

class CCertificateur(faust.Record):
    Certificateur: str
    # as we do not know yet the certificateur ID
    # id_certificateur

class CDiplomeCertificateur(faust.Record):
    id_diplome: int
    Certificateur: str

class CCodeIdeo2(faust.Record):
    CodeIdeo2: str
    # as we do not know yet the codeideo2 ID
    # id_ideo

class CDiplomeCodeIdeo2(faust.Record):
    id_diplome: int
    CodeIdeo2: str