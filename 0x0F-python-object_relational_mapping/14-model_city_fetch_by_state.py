#!/usr/bin/env python3
"""Script deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    session = Session(engine)
    stmt = session.query(State.id, State.name.\
        label('sname')).subquery()
    for s, cid, c in session.query(stmt.c.sname, City.id, City.name)\
        .join(stmt, City.state_id==stmt.c.id):
        print('{}: ({}) {}'.format(s, cid, c))
    session.close()
