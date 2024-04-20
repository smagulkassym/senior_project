from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db import DataEntry

# Set up the database engine and session
engine = create_engine('sqlite:///database/data.db')
Session = sessionmaker(bind=engine)

def get_data():
    session = Session()
    try:
        # Query all entries from the DataEntry table
        entries = session.query(DataEntry).all()

        # Convert each entry to a dictionary
        data = []
        for entry in entries:
            entry_data = {
                "id": entry.id,
                "nm_525": entry.nm_525,
                "nm_680": entry.nm_680,
                "nm_740": entry.nm_740,
                "nm_980": entry.nm_980,
                "nm_1450": entry.nm_1450,
                "nm_525_amb": entry.nm_525_amb,
                "nm_680_amb": entry.nm_680_amb,
                "nm_740_amb": entry.nm_740_amb,
                "nm_980_amb": entry.nm_980_amb,
                "nm_1450_amb": entry.nm_1450_amb,
                "longitude": entry.longitude,
                "latitude": entry.latitude,
                "tree_pos": entry.tree_pos,
            }
            data.append(entry_data)

        # Return the data as a JSON response
        return jsonify(data), 200
    except Exception as e:
        # Handle errors
        return f"Error retrieving data from the database: {str(e)}", 403
    finally:
        # Always close the session
        session.close()