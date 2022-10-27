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
    for row in session.query(State.id.label('sid'), State.name.
            label('sname'), City.id, City.name).join(State.cities)\
            .order_by(State.id).order_by(City.id).all():
        if row.sid not in lst:
            lst.append(row.sid)
            print('{}: {}'.format(row.sid, row.sname))
        print('    {}: {}'.format(row.id, row.name))
    session.close()
