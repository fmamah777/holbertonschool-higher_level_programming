#!/usr/bin/python3
"""
script lists all State objects from the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    dbengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True)

    Base.metadata.create_all(dbengine)
    dbsess = sessionmaker(bind=dbengine)

    for row in dbsession().query(State).order_by(State.id):
        print("{}: {}".format(row.id, row.name))

    dbsess().close
