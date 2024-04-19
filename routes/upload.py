from flask import Blueprint, request
from utils.save_image import save_image

upload = Blueprint('upload', __name__)

@upload.route("/upload", methods=["POST"])
def image():
    try:
        # Get the Base64 encoded image data from the request
        image_data = request.json['image']
        # image_data = request.json.get('image', None)

        if image_data is None:
            return {
                'success': False,
                'message': 'No image data found in the request'
            }, 400
        
        return save_image(image_data)
        
    except Exception as e:
        return f'Error: {str(e)}'
