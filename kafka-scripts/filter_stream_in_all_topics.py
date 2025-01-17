import faust
import csv
from io import StringIO


from class_kafka_scripts import CFullDiplome, CFullValidateur, CDiplomeCertificateur, CDiplomeCodeIdeo2, CDiplomeValidateur, CCertificateur, CCodeIdeo2


app = faust.App("csv_filter_app", broker="kafka://localhost:9092")





#note faust encoder only support raw/json/yaml/pickle/binary and not UTF-8, or "raw unicode" that we must .decode('utf-8)

input_topic = app.topic("streams-input-diplomes", value_serializer='raw')
output_topic_diplomes = app.topic("Diplomes")
output_topic_validateur = app.topic("Validateur")
output_topic_link_validateur_diplome = app.topic("Link_Validateur")
output_topic_certificateurs = app.topic("Certificateurs")
output_topic_link_certificateur_diplome = app.topic("Link_Certificateur")
output_topic_codeideo2 = app.topic("CodeIdeo2")
output_topic_link_codeideo2_diplome = app.topic("Link_CodeIdeo2")

#output_topic_test = app.topic("test")



@app.agent(input_topic)
async def process(stream):
    async for event in stream:
        event_utf8 = event.decode('utf-8')
        #print(f"debug: DECODED: {event_utf8}")
        mockup_csv = StringIO(event_utf8)
        fields = csv.reader(mockup_csv)
        for csv_row in fields:
            var_code_diplome = csv_row[0]
            var_libelle_diplome = csv_row[1]
            var_libelle_type_diplome = csv_row[2]
            var_code_niveau_europeen = csv_row[3]
            var_date_maj = csv_row[4]
            var_code_formacode = csv_row[5]
            var_libelle_formacode = csv_row[6]
            var_code_rome_1 = csv_row[7]
            var_code_rome_2 = csv_row[8]
            var_code_rome_3 = csv_row[9]
            var_code_rome_4 = csv_row[10]
            var_code_rome_5 = csv_row[11]
            var_code_nsf = csv_row[12]
            var_code_rncp = csv_row[13]
            var_code_rs = csv_row[14]
            var_code_scolarite = csv_row[15]
            var_validateur = csv_row[16]
            var_certificateur = csv_row[17]
            var_annee_premiere_session = csv_row[18]
            var_annee_derniere_session = csv_row[19]
            var_code_ancien_diplome = csv_row[20]
            var_intitule_ancien_diplome = csv_row[21]
            var_code_ancien_rncp = csv_row[22]
            var_code_ancien_scolarite = csv_row[23]
            var_etat = csv_row[24]
            var_etat_libelle = csv_row[25]
            var_etat_ancien_diplome = csv_row[26]
            var_etat_ancien_diplome_libelle = csv_row[27]
            var_accessibilite_fi = csv_row[28]
            var_accessibilite_ca = csv_row[29]
            var_accessibilite_fc = csv_row[30]
            var_accessibilite_cp = csv_row[31]
            var_accessibilite_vae = csv_row[32]
            var_accessibilite_ind = csv_row[33]
            var_code_type_diplome = csv_row[34]
            var_codeideo2 = csv_row[35]

        # var = Class(key=value, key=value)
        diplomes = CFullDiplome(Code_Diplome=var_code_diplome,Libelle_Diplome=var_libelle_diplome,Libelle_Type_Diplome=var_libelle_type_diplome,
                                Code_Niveau_Europeen=var_code_niveau_europeen,Date_MaJ=var_date_maj,Code_FormaCode=var_code_formacode,
                                Libelle_FormaCode=var_libelle_formacode,Code_Rome_1=var_code_rome_1,Code_Rome_2=var_code_rome_2,
                                Code_Rome_3=var_code_rome_3,Code_Rome_4=var_code_rome_4,Code_Rome_5=var_code_rome_5,Code_Nsf=var_code_nsf,
                                Code_RNCP=var_code_rncp,Code_RS=var_code_rs,Code_Scolarite=var_code_scolarite,
                                Annee_Premiere_Session=var_annee_premiere_session,Annee_Derniere_Session=var_annee_derniere_session,
                                Code_Ancien_Diplome=var_code_ancien_diplome,Intitule_Ancien_Diplome=var_intitule_ancien_diplome,
                                Code_Ancien_RNCP=var_code_ancien_rncp,Code_Ancien_Scolarite=var_code_ancien_scolarite,Etat=var_etat,
                                Etat_Libelle=var_etat_libelle,Etat_Ancien_Diplome=var_etat_ancien_diplome,
                                Etat_Ancien_Diplome_Libelle=var_etat_ancien_diplome_libelle,Accessibilite_fi=var_accessibilite_fi,
                                Accessibilite_ca=var_accessibilite_ca,Accessibilite_fc=var_accessibilite_fc,Accessibilite_cp=var_accessibilite_cp,
                                Accessibilite_vae=var_accessibilite_vae,Accessibilite_ind=var_accessibilite_ind,Code_type_diplome=var_code_type_diplome
                                )
        validateurs = CFullValidateur(Validateur=var_validateur)
        link_validateur_diplome = CDiplomeValidateur(id_diplome=var_code_diplome, Validateur=var_validateur)
        certificateurs = CCertificateur(Certificateur=var_certificateur)
        link_certificateur_diplome = CDiplomeCertificateur(id_diplome=var_code_diplome, Certificateur=var_certificateur)
        codeideo2 = CCodeIdeo2(CodeIdeo2=var_codeideo2)
        link_codeideo2_diplome = CDiplomeCodeIdeo2(id_diplome=var_code_diplome,CodeIdeo2=var_codeideo2)

        await output_topic_diplomes.send(value=diplomes)
        await output_topic_validateur.send(value=validateurs)
        await output_topic_link_validateur_diplome.send(value=link_validateur_diplome)
        await output_topic_certificateurs.send(value=certificateurs)
        await output_topic_link_certificateur_diplome.send(value=link_certificateur_diplome)
        await output_topic_codeideo2.send(value=codeideo2)
        await output_topic_link_codeideo2_diplome.send(value=link_codeideo2_diplome)



if __name__ == '__main__':
    app.main()