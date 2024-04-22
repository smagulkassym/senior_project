from flask import Blueprint, request, jsonify
from utils.validate_data import validate_data
from utils.save_data import save_data
from utils.get_data import get_data

new = Blueprint('new', __name__)

@new.route("/new", methods=["GET"])
def put_data():
    # Get query parameters from the URL
    query_params = {
        '365nm': request.args.get('365nm'),
        '365nm_amb': request.args.get('365nm_amb'),
        '405nm': request.args.get('405nm'),
        '405nm_amb': request.args.get('405nm_amb'),
        '525nm': request.args.get('525nm'),
        '525nm_amb': request.args.get('525nm_amb'),
        '680nm': request.args.get('680nm'),
        '680nm_amb': request.args.get('680nm_amb'),
        '740nm': request.args.get('740nm'),
        '740nm_amb': request.args.get('740nm_amb'),
        '980nm': request.args.get('980nm'),
        '980nm_amb': request.args.get('980nm_amb'),
        '1450nm': request.args.get('1450nm'),
        '1450nm_amb': request.args.get('1450nm_amb'),
        '0nm': request.args.get('0nm'),
        '0nm_amb': request.args.get('0nm_amb'),
        'longitude': request.args.get('longitude'),
        'latitude': request.args.get('latitude'),
        'tree_pos': request.args.get('tree_pos')
    }
    
    # Optionally convert numerical data to appropriate types
    # for key in query_params:
    #     if query_params[key] is not None and key not in ['tree_pos', 'longitude', 'latitude']:
    #         query_params[key] = int(query_params[key])
    #     elif key in ['longitude', 'latitude'] and query_params[key] is not None:
    #         query_params[key] = float(query_params[key])
        
    # data = query_params

    if validate_data(query_params):
        if save_data(query_params):
            return {
                "data" : query_params,
                "success": True,
                "message": "Data received and saved successfully!"
            }, 200
        else:
            return {
                "data" : query_params,
                "success": False,
                "message": "Data received successfully but failed to save"
            }, 403
    
    else:
        return {
            "data" : query_params,
            "success": False,
            "message": "Error: Missing fields in received data"
        }, 400
        # return data, 400
    
    # return jsonify({
    #     'success': True,
    #     'data': query_params
    # })