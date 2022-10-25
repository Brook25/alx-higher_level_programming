#!/usr/bin/python3
"""Script deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    session = Session(engine)
    """Here you can also loop over and delete
     returned objects using session.delete(obj)
    """
    session.query(State).filter(State.name.like('%a%'))\
        .delete(synchronize_session=False)
    session.commit()
    session.close()
