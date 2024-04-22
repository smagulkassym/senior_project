from flask import Blueprint, request
from utils.validate_data import validate_data
from utils.save_data import save_data
from utils.get_data import get_data

home_bp = Blueprint('home', __name__)

@home_bp.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            print(data)
        else:
            data = request.form.to_dict()
            print(data)
        # print("Data:", data)
        
        if validate_data(data):
            if save_data(data):
                return {
                    "data" : data,
                    "success": True,
                    "message": "Data received and saved successfully!"
                }, 200
            else:
                return {
                    "data" : data,
                    "success": False,
                    "message": "Data received successfully but failed to save"
                }, 403
        
        else:
            return {
                "data" : data,
                "success": False,
                "message": "Error: Missing fields in received data"
            }, 400
            # return data, 400
    
    if request.method == "GET":
        return get_data()
