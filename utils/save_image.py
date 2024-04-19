import base64, time

IMAGE_COUNTER = 0

def save_image(image_data):
    global IMAGE_COUNTER

    current_time = time.strftime("%Y%m%d_%H%M%S")
    filename = f'{current_time}_{IMAGE_COUNTER}'

    # Decode the Base64 encoded image data
    decoded_data = base64.b64decode(image_data)

    # Specify the file path where you want to save the image
    file_path = f'uploads/{filename}.jpg'  # Adjust the file path as needed

    # Save the decoded image data to a file
    with open(file_path, 'wb') as image_file:
        image_file.write(decoded_data)

    IMAGE_COUNTER += 1

    # return "Image uploaded successfully!", 200

    return {
        'success': True,
        'message': 'Image uploaded successfully!',
        'file_name': filename
    }, 200