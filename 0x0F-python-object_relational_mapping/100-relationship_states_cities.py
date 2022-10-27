#!/usr/bin/python3
"""Script adds the State object “California”
with the City “San Francisco”
to the database hbtn_0e_100_usa"""

if __name__ == "__main__":

    import sys
    from relationship_city import Base, City, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    san_f = City(name='San Francisco')
    san_f.state = State(name='California')
    session.add(san_f)
    session.commit()
    session.close()
