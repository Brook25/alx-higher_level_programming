#!/usr/bin/python3
"""
This script lists related state and city objects
in order of ids
"""

if __name__ == "__main__":
    from relationship_city import Base, City, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2], sys.argv[3]))

    session = Session(engine)
    for row in session.query(State).order_by(State.id):
        print('{}: {}'.format(row.id, row.name))
        for row1 in row.cities:
            print('    {}: {}'.format(row1.id, row1.name))
    session.close()
