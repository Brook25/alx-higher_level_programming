#!/usr/bin/python3
"""Script prints the first State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).order_by(State.id).first()
    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
    session.close()
