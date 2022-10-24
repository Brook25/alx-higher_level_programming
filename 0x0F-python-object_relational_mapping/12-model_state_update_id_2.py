#!/usr/bin/python3
"""Script changes the name of a State object from
the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    session = Session(engine)
    session.query(State).where(State.id == 2).update\
            ({State.name: 'New Mexico'})
    session.commit()
    session.close()
