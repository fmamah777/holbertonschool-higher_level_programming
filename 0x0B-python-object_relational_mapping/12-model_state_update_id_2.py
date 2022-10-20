#!/usr/bin/python3
"""
changes the name of the to given where id is a specific number
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
    dbs = dbsess()

    upstate = dbs.query(State).filter(State.id == 2).one()
    upstate.name = "New Mexico"
    dbs.commit()

    dbsess().close
