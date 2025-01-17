# Create a FastAPI app

# FastApi to use it; HTTPException to customize error response; Depends to verify db connection is up; status to customize reponse status1
from fastapi import FastAPI, HTTPException, Depends, status

# To declare type of a reference + add additional information
# FastAPI uses Annotated for data validation
from typing import Annotated

# To connect to the DB
from database import SessionLocal
from sqlalchemy.orm import Session, exc

# For queries with multiples values
from sqlalchemy import and_

# Import db model/class
import DB_models

# For datetime.date format in class
from datetime import date

# To search with option
from typing import Union

# Where all our class are defined
from my_class import FullDiplome, FullCertificateur, FullCodeIdeo2, FullDiplomeCertificateur, FullDiplomeCodeIdeo2, FullDiplomeValidateur, FullValidateur






########################################################################################################
#                                                                                                      #
#                                              START                                                   #
#                                                                                                      #
########################################################################################################

# instanciate the app
app = FastAPI()


# sql exception
db_exceptions = exc.sa_exc




# Initiate the DB connection
# do not forget to close the connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]



#########################################################
# CRUD Diplome
#########################################################
# get/get search on all parameters
# each parameters needs to be set manually or they are mandatory
# python decorator
@app.get("/diplome/search/")
def search_diplome(
    Code_Diplome: Union[int, None] = None,
    Libelle_Diplome: Union[str, None] = None,
    Libelle_Type_Diplome: Union[str, None] = None,
    Code_Niveau_Europeen: Union[int, None] = None,
    Date_MaJ: Union[date, None] = None,
    Code_FormaCode: Union[int, None] = None,
    Libelle_FormaCode: Union[str, None] = None,
    Code_Rome_1: Union[str, None] = None,
    Code_Rome_2: Union[str, None] = None,
    Code_Rome_3: Union[str, None] = None,
    Code_Rome_4: Union[str, None] = None,
    Code_Rome_5: Union[str, None] = None,
    Code_Nsf: Union[int, None] = None,
    Code_RNCP: Union[int, None] = None,
    Code_RS: Union[int, None] = None,
    Code_Scolarite: Union[str, None] = None,
    Annee_Premiere_Session: Union[int, None] = None,
    Annee_Derniere_Session: Union[int, None] = None,
    Code_Ancien_Diplome: Union[int, None] = None,
    Intitule_Ancien_Diplome: Union[str, None] = None,
    Code_Ancien_RNCP: Union[int, None] = None,
    Code_Ancien_Scolarite: Union[str, None] = None,
    Etat: Union[int, None] = None,
    Etat_Libelle: Union[str, None] = None,
    Etat_Ancien_Diplome: Union[int, None] = None,
    Etat_Ancien_Diplome_Libelle: Union[str, None] = None,
    Accessibilite_fi: Union[int, None] = None,
    Accessibilite_ca: Union[int, None] = None,
    Accessibilite_fc: Union[int, None] = None,
    Accessibilite_cp: Union[int, None] = None,
    Accessibilite_vae: Union[int, None] = None,
    Accessibilite_ind: Union[int, None] = None,
    Code_type_diplome: Union[int, None] = None,
    db: Session = Depends(get_db)
):
    """
    You can combine multiple value items
    """
    # initiate / reset at each call
    filter_list = []
    try:
        if Code_Diplome is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Diplome == Code_Diplome)
        if Libelle_Diplome is not None:
            filter_list.append(DB_models.DBDiplomes.Libelle_Diplome == Libelle_Diplome)
        if Libelle_Type_Diplome is not None:
            filter_list.append(DB_models.DBDiplomes.Libelle_Type_Diplome == Libelle_Type_Diplome)
        if Code_Niveau_Europeen is not None:
            filter_list.append(DB_models.DBDiplomes.Libelle_Type_Diplome == Libelle_Type_Diplome)
        if Date_MaJ is not None:
            filter_list.append(DB_models.DBDiplomes.Date_MaJ == Date_MaJ)
        if Code_FormaCode is not None:
            filter_list.append(DB_models.DBDiplomes.Code_FormaCode == Code_FormaCode)
        if Libelle_FormaCode is not None:
            filter_list.append(DB_models.DBDiplomes.Libelle_FormaCode == Libelle_FormaCode)
        if Code_Rome_1 is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Rome_1 == Code_Rome_1)
        if Code_Rome_2 is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Rome_2 == Code_Rome_2)
        if Code_Rome_3 is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Rome_3 == Code_Rome_3)
        if Code_Rome_4 is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Rome_4 == Code_Rome_4)
        if Code_Rome_5 is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Rome_5 == Code_Rome_5)
        if Code_Nsf is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Nsf == Code_Nsf)
        if Code_RNCP is not None:
            filter_list.append(DB_models.DBDiplomes.Code_RNCP == Code_RNCP)
        if Code_RS is not None:
            filter_list.append(DB_models.DBDiplomes.Code_RS == Code_RS)
        if Code_Scolarite is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Scolarite == Code_Scolarite)
        if Annee_Premiere_Session is not None:
            filter_list.append(DB_models.DBDiplomes.Annee_Premiere_Session == Annee_Premiere_Session)
        if Annee_Derniere_Session is not None:
            filter_list.append(DB_models.DBDiplomes.Annee_Derniere_Session == Annee_Derniere_Session)
        if Code_Ancien_Diplome is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Ancien_Diplome == Code_Ancien_Diplome)
        if Intitule_Ancien_Diplome is not None:
            filter_list.append(DB_models.DBDiplomes.Intitule_Ancien_Diplome == Intitule_Ancien_Diplome)
        if Code_Ancien_RNCP is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Ancien_RNCP == Code_Ancien_RNCP)
        if Code_Ancien_Scolarite is not None:
            filter_list.append(DB_models.DBDiplomes.Code_Ancien_Scolarite == Code_Ancien_Scolarite)
        if Etat is not None:
            filter_list.append(DB_models.DBDiplomes.Etat == Etat)
        if Etat_Libelle is not None:
            filter_list.append(DB_models.DBDiplomes.Etat_Libelle == Etat_Libelle)
        if Etat_Ancien_Diplome is not None:
            filter_list.append(DB_models.DBDiplomes.Etat_Ancien_Diplome == Etat_Ancien_Diplome)
        if Etat_Ancien_Diplome_Libelle is not None:
            filter_list.append(DB_models.DBDiplomes.Etat_Ancien_Diplome_Libelle == Etat_Ancien_Diplome_Libelle)
        if Accessibilite_fi is not None:
            filter_list.append(DB_models.DBDiplomes.Accessibilite_fi == Accessibilite_fi)
        if Accessibilite_ca is not None:
            filter_list.append(DB_models.DBDiplomes.Accessibilite_ca == Accessibilite_ca)
        if Accessibilite_fc is not None:
            filter_list.append(DB_models.DBDiplomes.Accessibilite_fc == Accessibilite_fc)
        if Accessibilite_cp is not None:
            filter_list.append(DB_models.DBDiplomes.Accessibilite_cp == Accessibilite_cp)
        if Accessibilite_vae is not None:
            filter_list.append(DB_models.DBDiplomes.Accessibilite_vae == Accessibilite_vae)
        if Accessibilite_ind is not None:
            filter_list.append(DB_models.DBDiplomes.Accessibilite_ind == Accessibilite_ind)
        if Code_type_diplome is not None:
            filter_list.append(DB_models.DBDiplomes.Code_type_diplome == Code_type_diplome)

        # check if empty, otherwise OOM => crash VM
        if len(filter_list) == 0:
            raise HTTPException(status_code=403, detail="FORBIDDEN - You must set at least one parameter")
        else: 
            diplome_get_full = db.query(DB_models.DBDiplomes).filter(and_(*filter_list)).first()
        return diplome_get_full
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")



# get/get 1 diplome by ID
@app.get("/diplome/{diplome_id}", status_code=status.HTTP_200_OK)
def read_diplome(diplome_id: int, db: db_dependency):
    """
    Put the ID of the desired diplome
    """
    try:
        # all() or first() needed otherwise crash
        diplome_get = db.query(DB_models.DBDiplomes).filter(DB_models.DBDiplomes.Code_Diplome == diplome_id).first()
        if diplome_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Diplome {diplome_id} not found")
        return diplome_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")



# post/create new diplome by ID
@app.post("/diplome/", status_code=status.HTTP_201_CREATED)
def create_diplome(diplome: FullDiplome, db: db_dependency):
    """
    Create a new diplome by setting the ID
    Mandatory fields:
    - Code_Diplome
    - Libelle_Diplome
    - Code_Niveau_Europeen
    """
    try:
        diplome_post = DB_models.DBDiplomes(**diplome.model_dump())
        db.add(diplome_post)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        # okay for our internal debug usage, not for PRD usage
        raise HTTPException(status_code=501, detail=f"INTERNAL ERROR - {e}")

# put/update diplome by ID
# keep the codediplome in URL as an idiotproof method
@app.put("/diplome/{diplome_id}", status_code=status.HTTP_201_CREATED)
def update_diplome(diplome_id: int, diplome: FullDiplome, db: db_dependency):
    """
    UPDATE an existing diplome by his ID
    """
    try:
        if diplome.Code_Diplome != diplome_id:
            raise HTTPException(status_code=403, detail=f"DENIED - Diplome requested \"{diplome_id}\" in path and diplome requested in body \"{diplome.Code_Diplome}\" are not the same")
        diplome_get = db.query(DB_models.DBDiplomes).filter(DB_models.DBDiplomes.Code_Diplome == diplome_id).first()
        if diplome_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Diplome with ID {diplome_id} not found")
        for key, value in diplome.model_dump().items():
            setattr(diplome_get, key, value)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

  
# delete/delete diplome by ID
@app.delete("/diplome/{diplome_id}", status_code=status.HTTP_200_OK)
def delete_diplome(diplome_id: int, db: db_dependency):
    """
    DELETE an existing diplome by his ID
    """
    try:
        diplome_delete = db.query(DB_models.DBDiplomes).filter(DB_models.DBDiplomes.Code_Diplome == diplome_id).first()
        if diplome_delete is None:
            raise HTTPException(status_code=404, detail=f"Diplome with ID {diplome_id} not found")
        db.delete(diplome_delete)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Internal Error - {e}")




########################################################
############## search by each category #################
########################################################


# get/get template for all category
# we use a like, for "big search", others should use the /diplomes/search for precise result
# .first() will always return a list even if no result, 
def get_diplome_by_field(field_name: str, field_value: str, db: db_dependency): 
    try: 
        query_filter = getattr(DB_models.DBDiplomes, field_name).like(f'%{field_value}%') 
        diplome_get = db.query(DB_models.DBDiplomes).filter(query_filter).all() 
        #all() always return a list, enven empty, so the check must be "if not xxx"
        if not diplome_get: 
            raise HTTPException(status_code=404, detail=f"NOT FOUND - {field_name} {field_value} not found") 
        return diplome_get 
    except db_exceptions.SQLAlchemyError as e: 
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}") 

@app.get("/diplomes/Libelle_Diplome/{libelle_diplome}", status_code=status.HTTP_200_OK) 
def read_libelle_diplome(libelle_diplome: str, db: db_dependency): 
    return get_diplome_by_field("Libelle_Diplome", libelle_diplome, db)

@app.get("/diplomes/Libelle_Type_Diplome/{libelle_type_diplome}", status_code=status.HTTP_200_OK) 
def read_libelle_type_diplome(libelle_type_diplome: str, db: db_dependency): 
    return get_diplome_by_field("Code_Niveau_Europeen", libelle_type_diplome, db)
    
@app.get("/diplomes/Code_Niveau_Europeen/{code_niveau_europeen}", status_code=status.HTTP_200_OK) 
def read_code_niveau_europeen(code_niveau_europeen: int, db: db_dependency): 
    return get_diplome_by_field("Code_Niveau_Europeen", code_niveau_europeen, db)

@app.get("/diplomes/Date_MaJ/{date_maj}", status_code=status.HTTP_200_OK)
def read_date_maj(date_maj: date, db: db_dependency):
    return get_diplome_by_field("Date_MaJ", date_maj, db)

@app.get("/diplomes/Code_FormaCode/{code_formacode}", status_code=status.HTTP_200_OK)
def read_code_formacode(code_formacode: int, db: db_dependency):
    return get_diplome_by_field("Code_FormaCode", code_formacode, db)

@app.get("/diplomes/Libelle_FormaCode/{libelle_formacode}", status_code=status.HTTP_200_OK)
def read_libelle_formacode(libelle_formacode: str, db: db_dependency):
    return get_diplome_by_field("Libelle_FormaCode", libelle_formacode, db)

@app.get("/diplomes/Code_Rome_1/{code_rome_1}", status_code=status.HTTP_200_OK)
def read_code_rome_1(code_rome_1: str, db: db_dependency):
    """limited to 5 character max"""
    return get_diplome_by_field("Code_Rome_1", code_rome_1, db)

@app.get("/diplomes/Code_Rome_2/{code_rome_2}", status_code=status.HTTP_200_OK)
def read_code_rome_2(code_rome_2: str, db: db_dependency):
    """limited to 5 character max"""
    return get_diplome_by_field("Code_Rome_2", code_rome_2, db)

@app.get("/diplomes/Code_Rome_3/{code_rome_3}", status_code=status.HTTP_200_OK)
def read_code_rome_3(code_rome_3: str, db: db_dependency):
    """limited to 5 character max"""
    return get_diplome_by_field("Code_Rome_3", code_rome_3, db)

@app.get("/diplomes/Code_Rome_4/{code_rome_4}", status_code=status.HTTP_200_OK)
def read_code_rome_4(code_rome_4: str, db: db_dependency):
    """limited to 5 character max"""
    return get_diplome_by_field("Code_Rome_4", code_rome_4, db)

@app.get("/diplomes/Code_Rome_5/{code_rome_5}", status_code=status.HTTP_200_OK)
def read_code_rome_5(code_rome_5: str, db: db_dependency):
    """limited to 5 character max"""
    return get_diplome_by_field("Code_Rome_5", code_rome_5, db)

@app.get("/diplomes/Code_Nsf/{code_nsf}", status_code=status.HTTP_200_OK)
def read_code_nsf(code_nsf: int, db: db_dependency):
    return get_diplome_by_field("Code_Nsf", code_nsf, db)

@app.get("/diplomes/Code_RNCP/{code_rncp}", status_code=status.HTTP_200_OK)
def read_code_rncp(code_rncp: int, db: db_dependency):
    return get_diplome_by_field("Code_RNCP", code_rncp, db)

@app.get("/diplomes/Code_RS/{code_rs}", status_code=status.HTTP_200_OK)
def read_code_rs(code_rs: int, db: db_dependency):
    return get_diplome_by_field("Code_RS", code_rs, db)

@app.get("/diplomes/Code_Scolarite/{code_scolarite}", status_code=status.HTTP_200_OK)
def read_code_scolarite(code_scolarite: str, db: db_dependency):
    return get_diplome_by_field("Code_Scolarite", code_scolarite, db)

@app.get("/diplomes/Annee_Premiere_Session/{annee_premiere_session}", status_code=status.HTTP_200_OK)
def read_annee_premiere_session(annee_premiere_session: int, db: db_dependency):
    return get_diplome_by_field("Annee_Premiere_Session", annee_premiere_session, db)

@app.get("/diplomes/Annee_Derniere_Session/{annee_derniere_session}", status_code=status.HTTP_200_OK)
def read_annee_derniere_session(annee_derniere_session: int, db: db_dependency):
    return get_diplome_by_field("Annee_Derniere_Session", annee_derniere_session, db)

@app.get("/diplomes/Code_Ancien_Diplome/{code_ancien_diplome}", status_code=status.HTTP_200_OK)
def read_code_ancien_diplome(code_ancien_diplome: int, db: db_dependency):
    return get_diplome_by_field("Code_Ancien_Diplome", code_ancien_diplome, db)

@app.get("/diplomes/Intitule_Ancien_Diplome/{intitule_ancien_diplome}", status_code=status.HTTP_200_OK)
def read_intitule_ancien_diplome(intitule_ancien_diplome: str, db: db_dependency):
    return get_diplome_by_field("Intitule_Ancien_Diplome", intitule_ancien_diplome, db)

@app.get("/diplomes/Code_Ancien_RNCP/{code_ancien_rncp}", status_code=status.HTTP_200_OK)
def read_code_ancien_rncp(code_ancien_rncp: int, db: db_dependency):
    return get_diplome_by_field("Code_Ancien_RNCP", code_ancien_rncp, db)

@app.get("/diplomes/Code_Ancien_Scolarite/{code_ancien_scolarite}", status_code=status.HTTP_200_OK)
def read_code_ancien_scolarite(code_ancien_scolarite: str, db: db_dependency):
    return get_diplome_by_field("Code_Ancien_Scolarite", code_ancien_scolarite, db)

@app.get("/diplomes/Etat/{etat}", status_code=status.HTTP_200_OK)
def read_etat(etat: int, db: db_dependency):
    return get_diplome_by_field("Etat", etat, db)

@app.get("/diplomes/Etat_Libelle/{etat_libelle}", status_code=status.HTTP_200_OK)
def read_etat_libelle(etat_libelle: str, db: db_dependency):
    return get_diplome_by_field("Etat_Libelle", etat_libelle, db)

@app.get("/diplomes/Etat_Ancien_Diplome/{etat_ancien_diplome}", status_code=status.HTTP_200_OK)
def read_etat_ancien_diplome(etat_ancien_diplome: int, db: db_dependency):
    return get_diplome_by_field("Etat_Ancien_Diplome", etat_ancien_diplome, db)

@app.get("/diplomes/Etat_Ancien_Diplome_Libelle/{etat_ancien_diplome_libelle}", status_code=status.HTTP_200_OK)
def read_etat_ancien_diplome_libelle(etat_ancien_diplome_libelle: str, db: db_dependency):
    return get_diplome_by_field("Etat_Ancien_Diplome_Libelle", etat_ancien_diplome_libelle, db)

@app.get("/diplomes/Accessibilite_fi/{accessibilite_fi}", status_code=status.HTTP_200_OK)
def read_accessibilite_fi(accessibilite_fi: int, db: db_dependency):
    return get_diplome_by_field("Accessibilite_fi", accessibilite_fi, db)

@app.get("/diplomes/Accessibilite_ca/{accessibilite_ca}", status_code=status.HTTP_200_OK)
def read_accessibilite_ca(accessibilite_ca: int, db: db_dependency):
    return get_diplome_by_field("Accessibilite_ca", accessibilite_ca, db)

@app.get("/diplomes/Accessibilite_fc/{accessibilite_fc}", status_code=status.HTTP_200_OK)
def read_accessibilite_fc(accessibilite_fc: int, db: db_dependency):
    return get_diplome_by_field("Accessibilite_fc", accessibilite_fc, db)

@app.get("/diplomes/Accessibilite_cp/{accessibilite_cp}", status_code=status.HTTP_200_OK)
def read_accessibilite_cp(accessibilite_cp: int, db: db_dependency):
    return get_diplome_by_field("Accessibilite_cp", accessibilite_cp, db)

@app.get("/diplomes/Accessibilite_vae/{accessibilite_vae}", status_code=status.HTTP_200_OK)
def read_accessibilite_vae(accessibilite_vae: int, db: db_dependency):
    return get_diplome_by_field("Accessibilite_vae", accessibilite_vae, db)

@app.get("/diplomes/Accessibilite_ind/{accessibilite_ind}", status_code=status.HTTP_200_OK)
def read_accessibilite_ind(accessibilite_ind: int, db: db_dependency):
    return get_diplome_by_field("Accessibilite_ind", accessibilite_ind, db)

@app.get("/diplomes/Code_type_diplome/{code_type_diplome}", status_code=status.HTTP_200_OK)
def read_code_type_diplome(code_type_diplome: int, db: db_dependency):
    return get_diplome_by_field("Code_type_diplome", code_type_diplome, db)









#################################################################
######################## add validateur #########################
#################################################################
# CRUD
# get/get 1 diplome by ID
@app.get("/validateur/{validateur_id}", status_code=status.HTTP_200_OK)
def read_validateur(id: int, db: db_dependency):
    """
    Put the ID of the desired validateur
    """
    try:
        #all() or first() needed otherwise crash
        validateur_get = db.query(DB_models.DBValidateurs).filter(DB_models.DBValidateurs.id == id).first()
        if validateur_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Validateur {id} not found")
        return validateur_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")


# get/get 1 validateur by Name
@app.get("/validateur/", status_code=status.HTTP_200_OK)
def read_validateur_by_name(validateur_name: str, db: db_dependency):
    """
    Put the Name of the desired validateur
    If you want to edit, you need to do it by ID
    """
    try:
        validateur_by_name_get = db.query(DB_models.DBValidateurs).filter(DB_models.DBValidateurs.Validateur.like(f'%{validateur_name}%')).all()
        if not validateur_by_name_get:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Validateur {validateur_name} not found")
        return validateur_by_name_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")


# post/create new validateur by ID
@app.post("/validateur/", status_code=status.HTTP_201_CREATED)
def create_validateur(diplome: FullValidateur, db: db_dependency):
    """
    Create a new diplome by setting the ID
    Mandatory fields:
    - Code_Diplome
    - Libelle_Diplome
    - Code_Niveau_Europeen
    """
    try:
        validateur_post = DB_models.DBValidateurs(**diplome.model_dump())
        db.add(validateur_post)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        # okay for our internal debug usage, not for PRD usage
        raise HTTPException(status_code=501, detail=f"INTERNAL ERROR - {e}")

# put/update diplome by ID
# keep the codediplome in URL as an idiotproof method
@app.put("/validateur/{validateur_id}", status_code=status.HTTP_201_CREATED)
def update_validateur(validateur_id: int, validateur: FullValidateur, db: db_dependency):
    """
    UPDATE an existing validateur by his ID
    """
    try:
        if validateur.id != validateur_id:
            raise HTTPException(status_code=403, detail=f"DENIED - Validateur requested \"{validateur_id}\" in path and validateur requested in body \"{validateur.id}\" are not the same")
        validateur_get = db.query(DB_models.DBValidateurs).filter(DB_models.DBValidateurs.id == validateur_id).first()
        if validateur_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Validateur with ID {validateur_id} not found")
        for key, value in validateur.model_dump().items():
            setattr(validateur_get, key, value)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

  
# delete/delete diplome by ID
@app.delete("/validateur/{validateur_id}", status_code=status.HTTP_200_OK)
def delete_validateur(validateur_id: int, db: db_dependency):
    """
    DELETE an existing validateur by his ID
    """
    try:
        validateur_delete = db.query(DB_models.DBValidateurs).filter(DB_models.DBValidateurs.id == validateur_id).first()
        if validateur_delete is None:
            raise HTTPException(status_code=404, detail=f"Validateur with ID {validateur_id} not found")
        db.delete(validateur_delete)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Internal Error - {e}")









##################################################################
############## add join validateur/diplome
#################################################################
# CRUD

# get/get 1 diplome by ID
@app.get("/diplomesvalidateur/{diplomesvalidateur_id}", status_code=status.HTTP_200_OK)
def read_diplomesvalidateur(diplomesvalidateur_id: int, db: db_dependency):
    """
    Write the ID of the desired diplome, to see all the association
    """
    try:
        #all() or first() needed otherwise crash
        diplomesvalidateur_get = db.query(DB_models.DBDiplomesValidateur).filter(DB_models.DBDiplomesValidateur.id_diplome == diplomesvalidateur_id).first()
        if diplomesvalidateur_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Diplome with ID {diplomesvalidateur_id} not found in diplome-validateur association")
        return diplomesvalidateur_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

# get/get 1 diplome by ID
@app.get("/validateur-diplome/{validateur_diplome_id}", status_code=status.HTTP_200_OK)
def read_validateur_diplome(validateur_diplome_id: int, db: db_dependency):
    """
    Write the ID of the desired validateur, to see all the association
    """
    try:
        #all() or first() needed otherwise crash
        validateur_diplome_get = db.query(DB_models.DBDiplomesValidateur).filter(DB_models.DBDiplomesValidateur.id_validateur == validateur_diplome_id).first()
        if validateur_diplome_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Validateur with ID {validateur_diplome_id} not found in validateur-diplome association")
        return validateur_diplome_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")


# post/create new diplome by ID
@app.post("/diplomesvalidateur/", status_code=status.HTTP_201_CREATED)
def create_diplomesvalidateur(diplome: FullDiplomeValidateur, db: db_dependency):
    """
    Create a new diplomesvalidateur by setting the ID
    """
    try:
        diplomevalidateur_post = DB_models.DBDiplomesValidateur(**diplome.model_dump())
        db.add(diplomevalidateur_post)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        # okay for our internal debug usage, not for PRD usage
        raise HTTPException(status_code=501, detail=f"INTERNAL ERROR - {e}")

###############################################
### No update on join, delete or create it. ###
###############################################

  
# delete/delete diplome by ID
@app.delete("/diplomesvalidateur/", status_code=status.HTTP_200_OK)
def delete_diplomesvalidateur(diplomesvalidateur_id: FullDiplomeValidateur, db: db_dependency):
    """
    DELETE an existing diplomesvalidateur link by its ID
    """
    try:
        diplomesvalidateur_delete = db.query(DB_models.DBDiplomesValidateur).filter(DB_models.DBDiplomesValidateur.id_diplome == diplomesvalidateur_id.id_diplome).filter(DB_models.DBDiplomesValidateur.id_validateur == diplomesvalidateur_id.id_validateur).first()
        if diplomesvalidateur_delete is None:
            raise HTTPException(status_code=404, detail=f"Diplome with ID {diplomesvalidateur_id.id_diplome} and Validateur ID {diplomesvalidateur_id.id_validateur} not found")
        db.delete(diplomesvalidateur_delete)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Internal Error - {e}")






###########################################
############## add certificateur
###########################################
# CRUD

# get/get 1 diplome by ID
@app.get("/certificateur/{certificateur_id}", status_code=status.HTTP_200_OK)
def read_certificateur(certificateur_id: int, db: db_dependency):
    """
    Put the ID of the desired certificateur
    """
    try:
        #all() or first() needed otherwise crash
        certificateur_get = db.query(DB_models.DBCertificateurs).filter(DB_models.DBCertificateurs.id == certificateur_id).first()
        if certificateur_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - certificateur {certificateur_id} not found")
        return certificateur_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

# get/get 1 certificateur by Name
@app.get("/certificateur/", status_code=status.HTTP_200_OK)
def read_certificateur_by_name(certificateur_name: str, db: db_dependency):
    """
    Put the Name of the desired certificateur
    If you want to edit, you need to do it by ID
    """
    try:
        certificateur_by_name_get = db.query(DB_models.DBCertificateurs).filter(DB_models.DBCertificateurs.Certificateur.like(f'%{certificateur_name}%')).all()
        if not certificateur_by_name_get:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - certificateur {certificateur_name} not found")
        return certificateur_by_name_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

# post/create new diplome by ID
@app.post("/certificateur/", status_code=status.HTTP_201_CREATED)
def create_certificateur(certificateur: FullCertificateur, db: db_dependency):
    """
    Create a new certificateur by setting the ID
    """
    try:
        certificateur_post = DB_models.DBDiplomes(**certificateur.model_dump())
        db.add(certificateur_post)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        # okay for our internal debug usage, not for PRD usage
        raise HTTPException(status_code=501, detail=f"INTERNAL ERROR - {e}")

# put/update diplome by ID
# keep the certificateur_id in URL as an idiotproof method
@app.put("/certificateur/{certificateur_id}", status_code=status.HTTP_201_CREATED)
def update_certificateur(certificateur_id: int, certificateur: FullCertificateur, db: db_dependency):
    """
    UPDATE an existing certificateur by his ID
    """
    try:
        if certificateur.id != certificateur_id:
            raise HTTPException(status_code=403, detail=f"DENIED - certificateur requested \"{certificateur_id}\" in path and certificateur requested in body \"{certificateur.id}\" are not the same")
        certificateur_get = db.query(DB_models.DBCertificateurs).filter(DB_models.DBCertificateurs.id == certificateur_id).first()
        if certificateur_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - certificateur with ID {certificateur_id} not found")
        for key, value in certificateur.model_dump().items():
            setattr(certificateur_get, key, value)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

  
# delete/delete certificateur by ID
@app.delete("/certificateur/{certificateur_id}", status_code=status.HTTP_200_OK)
def delete_certificateur(certificateur_id: int, db: db_dependency):
    """
    DELETE an existing certificateur by his ID
    """
    try:
        certificateur_delete = db.query(DB_models.DBCertificateurs).filter(DB_models.DBCertificateurs.id == certificateur_id).first()
        if certificateur_delete is None:
            raise HTTPException(status_code=404, detail=f"Certificateur with ID {certificateur_id} not found")
        db.delete(certificateur_delete)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Internal Error - {e}")





####################################################
############## add join certificateur/diplome
###################################################
# CRUD


# get/get 1 diplome by ID
@app.get("/diplomescertificateur/{diplomecertificateur_id}", status_code=status.HTTP_200_OK)
def read_diplomecertificateur(diplomecertificateur_id: int, db: db_dependency):
    """
    Put the ID of the desired diplome to see the association
    """
    try:
        #all() or first() needed otherwise crash
        diplomecertificateur_get = db.query(DB_models.DBDiplomesCertificateur).filter(DB_models.DBDiplomesCertificateur.id_diplome == diplomecertificateur_id).first()
        if diplomecertificateur_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Diplomevalidateur ID {diplomecertificateur_id} not found")
        return diplomecertificateur_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

# get/get certificateur and diplomes
@app.get("/certificateur-diplome/{certificateurdiplome_id}", status_code=status.HTTP_200_OK)
def read_certificateur_diplome(certificateurdiplome_id: int, db: db_dependency):
    """
    Put the ID of the desired certificateur to see the association
    """
    try:
        #all() or first() needed otherwise crash
        certificateur_diplome_get = db.query(DB_models.DBDiplomesCertificateur).filter(DB_models.DBDiplomesCertificateur.id_certificateur == certificateurdiplome_id).first()
        if certificateur_diplome_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Certificateur ID {certificateurdiplome_id} not found")
        return certificateur_diplome_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")


# post/create new diplome by ID
@app.post("/diplomescertificateur/", status_code=status.HTTP_201_CREATED)
def create_diplomescertificateur(diplome: FullDiplomeCertificateur, db: db_dependency):
    """
    Create a new diplomescertificateur by setting the ID
    """
    try:
        diplomecertificateur_post = DB_models.DBDiplomesCertificateur(**diplome.model_dump())
        db.add(diplomecertificateur_post)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        # okay for our internal debug usage, not for PRD usage
        raise HTTPException(status_code=501, detail=f"INTERNAL ERROR - {e}")
    
###############################################
### No update on join, delete or create it. ###
###############################################

# delete/delete diplome by ID
@app.delete("/diplomescertificateur/", status_code=status.HTTP_200_OK)
def delete_diplomescertificateur(diplomesvalidateur_id: FullDiplomeValidateur, db: db_dependency):
    """
    DELETE an existing diplomesvalidateur link by its ID
    """
    try:
        diplomesvalidateur_delete = db.query(DB_models.DBDiplomesValidateur).filter(DB_models.DBDiplomesValidateur.id_diplome == diplomesvalidateur_id.id_diplome).filter(DB_models.DBDiplomesValidateur.id_validateur == diplomesvalidateur_id.id_validateur).first()
        if diplomesvalidateur_delete is None:
            raise HTTPException(status_code=404, detail=f"Diplome with ID {diplomesvalidateur_id.id_diplome} and Validateur ID {diplomesvalidateur_id.id_validateur} not found")
        db.delete(diplomesvalidateur_delete)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Internal Error - {e}")





######################################
############## add codeideo2 #########
######################################
# CRUD

# get/get 1 diplome by ID
@app.get("/codeideo2/{codeideo2_id}", status_code=status.HTTP_200_OK)
def read_codeideo2(codeideo2_id: int, db: db_dependency):
    """
    Put the ID of the desired codeideo2
    """
    try:
        #all() or first() needed otherwise crash
        codeideo2_get = db.query(DB_models.DBCodeIdeo2).filter(DB_models.DBCodeIdeo2.id == codeideo2_id).first()
        if codeideo2_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - codeideo2 {codeideo2_id} not found")
        return codeideo2_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")



# get/get codeideo2 by name
@app.get("/codeideo2/", status_code=status.HTTP_200_OK)
def read_codeideo2_by_name(codeideo2_name: str, db: db_dependency):
    """
    Put the Name of the desired codeideo2
    If you want to edit, you need to do it by ID
    """
    try:
        codeideo2_by_name_get = db.query(DB_models.DBCodeIdeo2).filter(DB_models.DBCodeIdeo2.CodeIdeo2.like(f'%{codeideo2_name}%')).all()
        if not codeideo2_by_name_get:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - codeideo2 {codeideo2_name} not found")
        return codeideo2_by_name_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")
    


# put/update codeideo2 by ID
# keep the codeideo2 in URL as an idiotproof method
@app.put("/codeideo2/{codeideo2_id}", status_code=status.HTTP_201_CREATED)
def update_codeideo2(codeideo2_id: int, codeideo2: FullCodeIdeo2, db: db_dependency):
    """
    UPDATE an existing codeideo2 by his ID
    """
    try:
        if codeideo2.id != codeideo2_id:
            raise HTTPException(status_code=403, detail=f"DENIED - codeideo2 requested \"{codeideo2_id}\" in path and diplome requested in body \"{codeideo2.id}\" are not the same")
        codeideo2_get = db.query(DB_models.DBCodeIdeo2).filter(DB_models.DBCodeIdeo2.id == codeideo2_id).first()
        if codeideo2_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - codeideo2 with ID {codeideo2_id} not found")
        for key, value in codeideo2.model_dump().items():
            setattr(codeideo2_get, key, value)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

  
# delete/delete codeideo2 by ID
@app.delete("/codeideo2/{codeideo2_id}", status_code=status.HTTP_200_OK)
def delete_codeideo2(codeideo2_id: int, db: db_dependency):
    """
    DELETE an existing codeideo2 by his ID
    """
    try:
        codeideo2_delete = db.query(DB_models.DBCodeIdeo2).filter(DB_models.DBCodeIdeo2.id == codeideo2_id).first()
        if codeideo2_delete is None:
            raise HTTPException(status_code=404, detail=f"CodeIdeo2 with ID {codeideo2_id} not found")
        db.delete(codeideo2_delete)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Internal Error - {e}")













#################################################
############## add join codeideo2/diplome #######
#################################################
# CRUD

# get/get diplome/codeideo2 by ID
@app.get("/diplomescodeideo2/{diplomecodeideo2_id}", status_code=status.HTTP_200_OK)
def read_diplomecodeideo2(diplomecodeideo2_id: int, db: db_dependency):
    """
    Get the association of the desired diplome for diplome/codeideo2
    """
    try:
        #all() or first() needed otherwise crash
        diplomecodeideo2_get = db.query(DB_models.DBDiplomesCodeIdeo2).filter(DB_models.DBDiplomesCodeIdeo2.id_diplome == diplomecodeideo2_id).first()
        if diplomecodeideo2_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - Diplome {diplomecodeideo2_id} not found")
        return diplomecodeideo2_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")

# get/get codeideo2/diplome by ID
@app.get("/codeideo2-diplome/{diplomecodeideo2_id}", status_code=status.HTTP_200_OK)
def read_codeideo2_diplome(codeideo2_by_id: int, db: db_dependency):
    """
    Get the association of the desired diplome for diplome/codeideo2
    """
    try:
        #all() or first() needed otherwise crash
        diplomecodeideo2_get = db.query(DB_models.DBDiplomesCodeIdeo2).filter(DB_models.DBDiplomesCodeIdeo2.id_ideo == codeideo2_by_id).first()
        if diplomecodeideo2_get is None:
            raise HTTPException(status_code=404, detail=f"NOT FOUND - CodeIdeo2 {codeideo2_by_id} not found")
        return diplomecodeideo2_get
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"INTERNAL ERROR - {e}")


# post/create new diplome by ID
@app.post("/diplomescodeideo2/", status_code=status.HTTP_201_CREATED)
def create_diplomescodeideo2(diplome: FullDiplomeCodeIdeo2, db: db_dependency):
    """
    Create a new diplomes/codeideo2 by setting the ID
    """
    try:
        diplomecodeideo2_post = DB_models.DBDiplomesCodeIdeo2(**diplome.model_dump())
        db.add(diplomecodeideo2_post)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        # okay for our internal debug usage, not for PRD usage
        raise HTTPException(status_code=501, detail=f"INTERNAL ERROR - {e}")
    
###############################################
### No update on join, delete or create it. ###
###############################################

# delete/delete diplome by ID
@app.delete("/diplomescodeideo2/", status_code=status.HTTP_200_OK)
def delete_diplomescodeideo2(diplomescodeideo2: FullDiplomeCodeIdeo2, db: db_dependency):
    """
    DELETE an existing diplomes/codeideo2 link by ID
    """
    try:
        diplomescodeideo2_delete = db.query(DB_models.DBDiplomesCodeIdeo2).filter(DB_models.DBDiplomesCodeIdeo2.id_diplome == diplomescodeideo2.id_diplome).filter(DB_models.DBDiplomesCodeIdeo2.id_ideo == diplomescodeideo2.id_ideo).first()
        if diplomescodeideo2_delete is None:
            raise HTTPException(status_code=404, detail=f"Diplome with ID {diplomescodeideo2.id_diplome} and CodeIdeo2 ID {diplomescodeideo2.id_ideo} not found")
        db.delete(diplomescodeideo2_delete)
        db.commit()
    except db_exceptions.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Internal Error - {e}")
