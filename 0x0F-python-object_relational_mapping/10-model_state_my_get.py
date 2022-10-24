#!/usr/bin/python3
"""Script adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))

    session = Session(engine)
    state = session.query(State.id).filter_by(name=sys.argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
