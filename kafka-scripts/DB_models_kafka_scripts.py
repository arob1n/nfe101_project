from datetime import date
# Define all the table existing, to return response easily
from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

# declarative class
class DBDiplomes(Base):
    __tablename__ = 'Diplomes'

    # index means we will be using it to search in the DB
    Code_Diplome: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    Libelle_Diplome: Mapped[str] = mapped_column(String(255), nullable=False)
    Libelle_Type_Diplome: Mapped[str] = mapped_column(String(255), nullable=False)
    Code_Niveau_Europeen: Mapped[Optional[int]]
    Date_MaJ: Mapped[Optional[date]]
    Code_FormaCode: Mapped[Optional[int]]
    Libelle_FormaCode: Mapped[Optional[str]] = mapped_column(String(255))
    Code_Rome_1: Mapped[Optional[str]] = mapped_column(String(5))
    Code_Rome_2: Mapped[Optional[str]] = mapped_column(String(5))
    Code_Rome_3: Mapped[Optional[str]] = mapped_column(String(5))
    Code_Rome_4: Mapped[Optional[str]] = mapped_column(String(5))
    Code_Rome_5: Mapped[Optional[str]] = mapped_column(String(5))
    Code_Nsf: Mapped[Optional[int]]
    Code_RNCP: Mapped[Optional[int]]
    Code_RS: Mapped[Optional[int]]
    Code_Scolarite: Mapped[Optional[str]] = mapped_column(String(255))
    Annee_Premiere_Session: Mapped[Optional[int]]
    Annee_Derniere_Session: Mapped[Optional[int]]
    Code_Ancien_Diplome: Mapped[Optional[int]]
    Intitule_Ancien_Diplome: Mapped[Optional[str]] = mapped_column(String(255))
    Code_Ancien_RNCP: Mapped[Optional[int]]
    Code_Ancien_Scolarite: Mapped[Optional[str]] = mapped_column(String(8))
    Etat: Mapped[Optional[int]]
    Etat_Libelle: Mapped[Optional[str]] = mapped_column(String(100))
    Etat_Ancien_Diplome: Mapped[Optional[int]]
    Etat_Ancien_Diplome_Libelle: Mapped[Optional[str]] = mapped_column(String(100))
    Accessibilite_fi: Mapped[Optional[int]]
    Accessibilite_ca: Mapped[Optional[int]]
    Accessibilite_fc: Mapped[Optional[int]]
    Accessibilite_cp: Mapped[Optional[int]]
    Accessibilite_vae: Mapped[Optional[int]]
    Accessibilite_ind: Mapped[Optional[int]]
    Code_type_diplome: Mapped[Optional[int]]

#   # Relationship to JoinDB
#   Join_validateurs = relationship("DBDiplomesValidateur", back_populates="JoinDB_diplomes")#, foreign_keys="[AAAADiplomesValidateurs.id_diplome]")
#   Join_certificateurs = relationship("DBDiplomesCertificateur", back_populates="JoinDB_diplomes")#, foreign_keys="[DiplomesCertificateur.id_diplome]")
#   Join_codeideo = relationship("DBDiplomesCodeIdeo2", back_populates="JoinDB_diplomes")#, foreign_keys="[DiplomesCodeIdeo2.id_diplome]")

################

class DBValidateurs(Base):
    __tablename__ = 'Validateurs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Validateur: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relationship for join
#    Join_diplomes_validateur = relationship("DBDiplomesValidateur", back_populates="JoinDB_validateurs", foreign_keys="[DBDiplomesValidateur.id_validateur]")

class DBDiplomesValidateur(Base):
    __tablename__ = 'DiplomesValidateur'
    id_diplome: Mapped[int] = mapped_column(Integer, ForeignKey("Diplomes.Code_Diplome"), primary_key=True)
    id_validateur: Mapped[int] = mapped_column(Integer, ForeignKey("Validateurs.id"), primary_key=True)
    
    # Add cascade so when we delete 1 entry it is also deleted on the Join Table
    # Join Validateurs and Diplomes
#    JoinDB_validateurs = relationship("DBValidateurs", back_populates="Join_diplomes_validateur", cascade="all,delete")
#    JoinDB_diplomes = relationship("DBDiplomes", back_populates="Join_validateurs", cascade="all,delete")


#############

class DBCertificateurs(Base):
    __tablename__ = 'Certificateurs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Certificateur: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relationship for join
#    Join_diplomes_certificateur = relationship("DBDiplomesCertificateur", back_populates="JoinDB_certificateurs")

class DBDiplomesCertificateur(Base):
    __tablename__ = 'DiplomesCertificateur'
    id_diplome: Mapped[int] = mapped_column(Integer, ForeignKey("Diplomes.Code_Diplome"), primary_key=True)
    id_certificateur: Mapped[int] = mapped_column(Integer, ForeignKey("Diplomes.Code_Diplome"), primary_key=True)

    # Relationship for join
#   JoinDB_certificateurs = relationship("DBCertificateurs", back_populates="Join_diplomes_certificateur", cascade="all,delete")
#   JoinDB_diplomes = relationship("DBDiplomes", back_populates="Join_certificateurs", cascade="all,delete")

###############

class DBCodeIdeo2(Base):
    __tablename__ = 'CodeIdeo2'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    CodeIdeo2: Mapped[str] = mapped_column(String(15), nullable=False)

    # join table
#    Join_diplomes_codeideo2 = relationship("DBDiplomesCertificateur", back_populates="JoinDB_codeideo")

class DBDiplomesCodeIdeo2(Base):
    __tablename__= 'DiplomesCodeIdeo2'
    id_diplome: Mapped[int] = mapped_column(Integer, ForeignKey("Diplomes.Code_Diplome"), primary_key=True)
    id_ideo: Mapped[int] = mapped_column(Integer, ForeignKey("CodeIdeo2.id"), primary_key=True)

    # join table
#    JoinDB_codeideo = relationship("DBCodeIdeo2", back_populates="Join_diplomes_codeideo2", cascade="all,delete")
#    JoinDB_diplomes = relationship("DBDiplomes", back_populates="Join_codeideo", cascade="all,delete")
