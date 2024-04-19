from flask import Blueprint, request
from utils.validate_data import validate_data
from utils.save_data import save_data

home_bp = Blueprint('home', __name__)

@home_bp.route("/", methods=["POST"])
def home():
    if request.method == "POST":
        data = request.get_json()
        # print("Data:", data)

        if validate_data(data):
            if save_data(data):
                return {
                    "success": True,
                    "message": "Data received and saved successfully!"
                }, 200
            else:
                return {
                    "success": False,
                    "message": "Data received successfully but failed to save"
                }, 403
        
        else:
            return {
                "success": False,
                "message": "Error: Missing fields in received data"
            }, 400