#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    try:
        # Query all State objects containing 'a' in their name
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

        # Delete each State object
        for state in states_to_delete:
            session.delete(state)

        # Commit the changes
        session.commit()
    finally:
        session.close()

if __name__ == "__main__":
    main()
