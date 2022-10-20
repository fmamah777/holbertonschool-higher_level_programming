#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':

    import sys
    import sqlalchemy
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    vtech = \
        create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                      sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    
    Base.metadata.create_all(vtech)
    Session = sessionmaker(bind=vtech)
    session = Session()
    novelty_state = session.query(State).filter_by(State.name.like('%a%'))
    for state in novelty_state:
        session.delete(state)
    session.commit()
    session.close()
