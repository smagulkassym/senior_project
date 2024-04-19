import json

from utils.save_data_to_db import save_data_to_db

def save_data(data):
    try:
        with open("database/received_data.txt", "a") as file:
            json.dump(data, file)
            file.write("\n")
        
        save_data_to_db(data)
        
        return True
    
    except Exception as e:
        print("Error saving data:", e)
        return False