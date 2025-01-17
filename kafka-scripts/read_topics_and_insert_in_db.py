from confluent_kafka import Consumer, KafkaException, KafkaError

# as faust send JSON objects
import json

# to connect to the DB
from database import SessionLocal, engine

# import db model/class
import DB_models_kafka_scripts

#were all our class are defined
from class_kafka_scripts import FullDiplome, FullCertificateur, FullCodeIdeo2, FullDiplomeCertificateur, FullDiplomeCodeIdeo2, FullDiplomeValidateur, FullValidateur






# create the DB if not present via the SQL scripts
# however the DB user needs important access that we might not want
#DB_models_kafka_scripts.Base.metadata.create_all(bind=engine)

# Define the function to convert integer values
# Limit it to int defined in CFullDiplome
def convert_to_int(data):
    list_to_update = ["Code_Niveau_Europeen", "Code_FormaCode","Code_Nsf","Code_RNCP","Code_RS","Annee_Premiere_Session",
                      "Annee_Derniere_Session","Code_Ancien_Diplome","Code_Ancien_RNCP","Etat","Etat_Ancien_Diplome",
                      "Accessibilite_fi","Accessibilite_ca","Accessibilite_fc","Accessibilite_cp","Accessibilite_vae",
                      "Accessibilite_ind","Code_type_diplome","id_diplome","id_certificateur", "id_validateur", "id_ideo"]
    for key, value in data.items():
        if key in list_to_update and isinstance(value, str) and value.isdigit():
            data[key] = int(value)
    return data


def change_empty_keys_to_null(data):
    for key, value in data.items():
        if value == "":
            data[key] = None
    return data

############################################################################################

def insert_diplomes(json_data: dict):
    # Parse the JSON data into a FullDiplome model
    full_diplome = FullDiplome(**json_data)

    session = SessionLocal()
    try:
        #use first
        diplome_get = session.query(DB_models_kafka_scripts.DBDiplomes).filter(DB_models_kafka_scripts.DBDiplomes.Code_Diplome == json_data["Code_Diplome"]).first()
        print(json_data["Code_Diplome"])
        print(diplome_get)
        #diplome_get=None
        if diplome_get is None:
            # to validate if data fit the class type
            diplome_post = DB_models_kafka_scripts.DBDiplomes(**full_diplome.model_dump())
            session.add(diplome_post)
            # We only need commit when INSERT/UPDATE/DELETE
            session.commit()
            print(f"New diplome with ID {json_data['Code_Diplome']} implemented")
        else:
            print(f"Diplome with Code_Diplome {json_data['Code_Diplome']} already exist")

    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()

################################################################################################


def insert_validateur(json_data: dict):
    # Parse JSON data into model

    session = SessionLocal()
    try:
    # search if name exist
        validateur_get = session.query(DB_models_kafka_scripts.DBValidateurs).filter(DB_models_kafka_scripts.DBValidateurs.Validateur == json_data["Validateur"]).first()
        if validateur_get is None:
            max_id = session.query(DB_models_kafka_scripts.DBValidateurs.id).order_by(DB_models_kafka_scripts.DBValidateurs.id.desc()).first()
            if max_id is not None:
                new_id = max_id[0] + 1
            else:
                new_id = 1
            json_data["id"] = new_id

            # validate the input
            complete_validateur = FullValidateur(**json_data)

            validateur_post = DB_models_kafka_scripts.DBValidateurs(**complete_validateur.model_dump())
            session.add(validateur_post)
            session.commit()
            print(f"New validateur with Name {json_data['Validateur']} and ID {json_data['id']} added to the database")
        else:
            print(f"Validateur with Name {json_data['Validateur']} already exists")
    
    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()
    
#################################################################################################


def insert_certificateur(json_data: dict):
    session = SessionLocal()
    try:
    # search if name exist
        certificateur_get = session.query(DB_models_kafka_scripts.DBCertificateurs).filter(DB_models_kafka_scripts.DBCertificateurs.Certificateur == json_data["Certificateur"]).first()
        if certificateur_get is None:
            max_id = session.query(DB_models_kafka_scripts.DBCertificateurs.id).order_by(DB_models_kafka_scripts.DBCertificateurs.id.desc()).first()
            if max_id is not None:
                new_id = max_id[0] + 1
            else:
                new_id = 1
            json_data["id"] = new_id

            # validate the input
            complete_certificateur = FullCertificateur(**json_data)

            certificateur_post = DB_models_kafka_scripts.DBCertificateurs(**complete_certificateur.model_dump())
            session.add(certificateur_post)
            session.commit()
            print(f"New certificateur with Name {json_data['Certificateur']} and ID {json_data['id']} added to the database")
        else:
            print(f"Certificateur with Name {json_data['Certificateur']} already exists")
    
    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()

############################################################################################################

def insert_codeideo2(json_data: dict):
    session = SessionLocal()
    try:
    # search if name exist
        codeideo2_get = session.query(DB_models_kafka_scripts.DBCodeIdeo2).filter(DB_models_kafka_scripts.DBCodeIdeo2.CodeIdeo2 == json_data["CodeIdeo2"]).first()
        if codeideo2_get is None:
            max_id = session.query(DB_models_kafka_scripts.DBCodeIdeo2.id).order_by(DB_models_kafka_scripts.DBCodeIdeo2.id.desc()).first()
            if max_id is not None:
                new_id = max_id[0] + 1
            else:
                new_id = 1
            json_data["id"] = new_id

            # validate the input
            complete_codeideo2 = FullCodeIdeo2(**json_data)

            codeideo2_post = DB_models_kafka_scripts.DBCodeIdeo2(**complete_codeideo2.model_dump())
            session.add(codeideo2_post)
            session.commit()
            print(f"New CodeIdeo2 with Name {json_data['CodeIdeo2']} and ID {json_data['id']} added to the database")
        else:
            print(f"CodeIdeo2 with Name {json_data['Validateur']} already exists")
    
    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()

################################################################################################


def insert_diplome_and_validateur(json_data: dict):
    session = SessionLocal()
    try:
        # search if name exist, and get the ID
        validateur_get = session.query(DB_models_kafka_scripts.DBValidateurs).filter(DB_models_kafka_scripts.DBValidateurs.Validateur == json_data["Validateur"]).first()
        
        # check validateur exists
        if validateur_get is None:
            print(f"Validateur with Name {json_data['Validateur']} does not exist")
            return
        
        # once validateur ID existence confirmed, add it to the json_data, and remove the Validateur name
        json_data["id_validateur"] = validateur_get.id
        json_data.pop("Validateur", None)

        # check diplome exists
        diplome_get = session.query(DB_models_kafka_scripts.DBDiplomes).filter(DB_models_kafka_scripts.DBDiplomes.Code_Diplome == json_data["id_diplome"]).first()
        if diplome_get is None:
            print(f"Diplome with ID {json_data['id_diplome']} does not exist")
            return
        
        # validate the input
        complete_link = FullDiplomeValidateur(**json_data)

        # if both exist, check if exist in link table
        link_get = session.query(DB_models_kafka_scripts.DBDiplomesValidateur).filter(
                                DB_models_kafka_scripts.DBDiplomesValidateur.id_diplome == json_data["id_diplome"],
                                DB_models_kafka_scripts.DBDiplomesValidateur.id_validateur == json_data["id_validateur"]
                                ).first()

        if link_get is None:
            link_post = DB_models_kafka_scripts.DBDiplomesValidateur(**complete_link.model_dump())
            session.add(link_post)
            session.commit()

            print(f"New link Diplome with ID {json_data['id_diplome']} and Validateur with ID {json_data['id_validateur']} added to the database")
        else:
            print(f"Link Diplome with ID {json_data['id_diplome']} and Validateur with ID {json_data['id_validateur']} already exists")
    
    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()

######################################################################################################


def insert_diplome_and_certificateur(json_data: dict):
    session = SessionLocal()
    try:
        # search if name exist, and get the ID
        certificateur_get = session.query(DB_models_kafka_scripts.DBCertificateurs).filter(DB_models_kafka_scripts.DBCertificateurs.Certificateur == json_data["Certificateur"]).first()
        
        # check validateur exists
        if certificateur_get is None:
            print(f"Certificateur with Name {json_data['Certificateur']} does not exist")
            return
        
        # once validateur ID existence confirmed, add it to the json_data, and remove the Validateur name
        json_data["id_certificateur"] = certificateur_get.id
        json_data.pop("Certificateur", None)

        # check diplome exists
        diplome_get = session.query(DB_models_kafka_scripts.DBDiplomes).filter(DB_models_kafka_scripts.DBDiplomes.Code_Diplome == json_data["id_diplome"]).first()
        if diplome_get is None:
            print(f"Diplome with ID {json_data['id_diplome']} does not exist")
            return
        
        # validate the input
        complete_link = FullDiplomeCertificateur(**json_data)

        # if both exist, check if exist in link_table
        link_get = session.query(DB_models_kafka_scripts.DBDiplomesCertificateur).filter(
                                DB_models_kafka_scripts.DBDiplomesCertificateur.id_diplome == json_data["id_diplome"],
                                DB_models_kafka_scripts.DBDiplomesCertificateur.id_certificateur == json_data["id_certificateur"]
                                ).first()

        if link_get is None:
            link_post = DB_models_kafka_scripts.DBDiplomesCertificateur(**complete_link.model_dump())
            session.add(link_post)
            session.commit()

            print(f"New link Diplome with ID {json_data['id_diplome']} and Certificateur with ID {json_data['id_certificateur']} added to the database")
        else:
            print(f"Link Diplome with ID {json_data['id_diplome']} and Certificateur with ID {json_data['id_certificateur']} already exists")
    
    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()


######################################################################################

def insert_diplome_and_codeideo2(json_data: dict):
    session = SessionLocal()
    try:
        # search if name exist, and get the ID
        codeideo2_get = session.query(DB_models_kafka_scripts.DBCodeIdeo2).filter(DB_models_kafka_scripts.DBCodeIdeo2.CodeIdeo2 == json_data["CodeIdeo2"]).first()
        
        # check validateur exists
        if codeideo2_get is None:
            print(f"CodeIdeo2 with Name {json_data['CodeIdeo2']} does not exist")
            return
        
        # once validateur ID existence confirmed, add it to the json_data, and remove the Validateur name
        json_data["id_ideo"] = codeideo2_get.id
        json_data.pop("CodeIdeo2", None)

        # check diplome exists
        diplome_get = session.query(DB_models_kafka_scripts.DBDiplomes).filter(DB_models_kafka_scripts.DBDiplomes.Code_Diplome == json_data["id_diplome"]).first()
        if diplome_get is None:
            print(f"Diplome with ID {json_data['id_diplome']} does not exist")
            return
        
        # validate the input
        complete_link = FullDiplomeCodeIdeo2(**json_data)

        # if both exist, check if exist in link table
        link_get = session.query(DB_models_kafka_scripts.DBDiplomesCodeIdeo2).filter(
                                DB_models_kafka_scripts.DBDiplomesCodeIdeo2.id_diplome == json_data["id_diplome"],
                                DB_models_kafka_scripts.DBDiplomesCodeIdeo2.id_ideo == json_data["id_ideo"]
                                ).first()

        if link_get is None:
            link_post = DB_models_kafka_scripts.DBDiplomesCodeIdeo2(**complete_link.model_dump())
            session.add(link_post)
            session.commit()

            print(f"New link Diplome with ID {json_data['id_diplome']} and CodeIdeo2 with ID {json_data['id_ideo']} added to the database")
        else:
            print(f"Link Diplome with ID {json_data['id_diplome']} and CodeIdeo2 with ID {json_data['id_ideo']} already exists")
    
    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()



######################################################################################################


def read_topics(topic: str):
    # Create the Consumer instance
    consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'CG-Diplomes'})
    consumer.subscribe([topic])

    # the first connection take 4s at least
    max_empty_topic_retry = 10
    empty_topic = 0

    print(f"Reading topic {topic}")
    try:
        while True:
            # Poll for a new message + timeout 1s, as default is infinite
            msg = consumer.poll(1.0)
            #msg_utf8 = msg.decode('utf-8')
            #print(msg_utf8)
            if msg is None:
                print("no message")
                empty_topic += 1
                if empty_topic >= max_empty_topic_retry:
                    print(f"Topic {topic} is empty since {empty_topic} tries")
                    break
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            
            print(f"RAW Received message: {msg.value().decode('utf-8')}")

            # Transform as correct JSON
            proper_message = msg.value().decode('utf-8')
            json_dict = json.loads(proper_message)
            # Remove the __faust key useless for us
            json_dict.pop("__faust", None)
            #print(type(json_dict))
            print(json.dumps(json_dict, ensure_ascii=False))

            json_dict = convert_to_int(json_dict)
            json_dict = change_empty_keys_to_null(json_dict)

            if topic == "Diplomes":
                insert_diplomes(json_dict)

            elif topic == "Validateur":
                # we receive validateur like:
                # { "validateur":"something;other;thing"}
                # we need to split it, to only insert one validateur at a time
                Validateur_dict = json_dict.get('Validateur')

                if Validateur_dict is not None:
                    # new list of dictionary
                    Validateur_array = [{'Validateur': validateur} for validateur in Validateur_dict.split(';')]
                    for x in Validateur_array:
                        insert_validateur(x)
                else:
                    print("Why do you want to insert type None ? Ignoring")

            elif topic == "Certificateurs":
                Certificateur_dict = json_dict.get('Certificateur')

                if Certificateur_dict is not None:
                    # new list of dictionary
                    Certificateur_array = [{'Certificateur': certificateur} for certificateur in Certificateur_dict.split(';')]
                    for x in Certificateur_array:
                        insert_certificateur(x)
                else:
                    print("Why do you want to insert type None ? Ignoring")

            elif topic == "CodeIdeo2":
                CodeIdeo2_dict = json_dict.get('CodeIdeo2')

                if CodeIdeo2_dict is not None:
                    # new list of dictionary
                    codeideo2_array = [{'CodeIdeo2': codeideo2} for codeideo2 in CodeIdeo2_dict.split(';')]
                    for x in codeideo2_array:
                        insert_codeideo2(x)
                else:
                    print("Why do you want to insert type None ? Ignoring")

            elif topic == "Link_Validateur":
                Diplome_dict = json_dict['id_diplome']
                Link_validateur_dict = json_dict.get('Validateur')

                if Link_validateur_dict is not None:
                    Link_validateur_array = [{'id_diplome': Diplome_dict, 'Validateur': link_validateur} for link_validateur in Link_validateur_dict.split(';')]
                    for x in Link_validateur_array:
                        insert_diplome_and_validateur(x)

            elif topic == "Link_Certificateur":
                Diplome_dict = json_dict['id_diplome']
                Link_certificateur_dict = json_dict.get('Certificateur')


                if Link_certificateur_dict is not None:
                    Link_certificateur_array = [{'id_diplome': Diplome_dict, 'Certificateur': link_certificateur} for link_certificateur in Link_certificateur_dict.split(';')]
                    for x in Link_certificateur_array:
                        insert_diplome_and_certificateur(x)
                else:
                    print("Why do you want to insert type None ? Ignoring")

            elif topic == "Link_CodeIdeo2":
                Diplome_dict = json_dict['id_diplome']
                Link_codeideo2_dict = json_dict.get('CodeIdeo2')

                if Link_codeideo2_dict is not None:
                    Link_codeideo2_array = [{'id_diplome': Diplome_dict, 'CodeIdeo2': link_codeideo2} for link_codeideo2 in Link_codeideo2_dict.split(';')]
                    for x in Link_codeideo2_array:
                        insert_diplome_and_codeideo2(x)
                else:
                    print("Why do you want to insert type None ? Ignoring")
                
            
            # We should check consumer lag to stop topic consumption
            # Use the timeout for this as of now

    except (KeyboardInterrupt, KafkaException, KafkaError) as e:
        print(e)
    finally:
        # Close the consumer, which will commit final offsets
        consumer.close()
        print("Topics read complete")


if __name__ == '__main__':
    read_topics("Diplomes")
    read_topics("Validateur")
    read_topics("Certificateurs")
    read_topics("CodeIdeo2")
    read_topics("Link_Validateur")
    read_topics("Link_Certificateur")
    read_topics("Link_CodeIdeo2")
    print("################################################")
    print("SYNC COMPLETE")
    exit()