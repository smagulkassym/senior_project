from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.db import DataEntry, Base

# Create the engine and session
engine = create_engine('sqlite:///database/data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_data_to_db(data):
    session = Session()
    try:
        # Create a new DataEntry instance using the received data
        entry = DataEntry(
            nm_525=data["525nm"],
            nm_680=data["680nm"],
            nm_740=data["740nm"],
            nm_980=data["980nm"],
            nm_1450=data["1450nm"],
            nm_525_amb=data["525nm_amb"],
            nm_680_amb=data["680nm_amb"],
            nm_740_amb=data["740nm_amb"],
            nm_980_amb=data["980nm_amb"],
            nm_1450_amb=data["1450nm_amb"],
            longitude=data["longitude"],
            latitude=data["latitude"],
            tree_pos=data["tree_pos"]
        )
        # Add the entry to the session
        session.add(entry)

        # Commit the session to save the changes to the database
        session.commit()

        print("id : ", entry.id)
    except Exception as e:
        # Rollback the session if an error occurs
        session.rollback()
        print("Error saving data to database:", e)
    finally:
        # Close the session
        session.close()