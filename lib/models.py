from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Specialty(Base):
    # linking a table to the class
    __tablename__ = "specialties"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/clinic.db', echo = True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    surgeon = Specialty("Surgeon")
    anchologist = Specialty("Anchologist")

    session.bulk_save_objects([surgeon, anchologist])

    session.commit()

    print(f"the new specialty id is {surgeon.id}")

    pecialties = session.query(Specialty).all()
    print([specialty.name for specialty in Specialty])


    session.query(Specialty).where(Specialty.id == 2).delete()
    session.commit()
