#!/usr/bin/python3
#!/usr/bin/python3
"""
script list states with 'a' in its name
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

    Astates = dbsess().query(State).order_by(State.id)\
        .filter(State.name.like("%a%"))

    for row in Astates:
        print("{}: {}".format(row.id, row.name))

    dbsess().close
