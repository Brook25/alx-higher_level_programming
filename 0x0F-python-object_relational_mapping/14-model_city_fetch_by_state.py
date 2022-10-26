#!/usr/bin/python3
"""This script prints all City objects
from the database hbtn_0e_14_usa"""

if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = session.query(State.id, State.name.label('sname')).subquery()
    for s, cid, c in session.query(stmt.c.sname, City.id, City.name).join(stmt, City.state_id==stmt.c.id):
        print('{}: ({}) {}'.format(s, cid, c))
    session.close()
