# file to connect to mariadb

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://DBU_NFE101:CeciEstUnProtoNFE101@localhost:3306/nfe_101?charset=utf8mb4'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)