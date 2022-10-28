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
                    .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    session = Session(engine)
    lst = []
    for s, c in session.query(State, City).join(State.cities).order_by(State.id):
        if s not in lst:
            lst.append(s)
            print('{}: {}'.format(s.id, s.name))
        print('    {}: {}'.format(c.id, c.name))
    session.close()
