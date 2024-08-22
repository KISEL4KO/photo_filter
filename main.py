from flask import Flask, request, jsonify
import opennsfw2 as n2
import os

# Initialize the Flask application
app = Flask(__name__)


# Define the route for checking NSFW images
@app.route('/check_nsfw', methods=['POST'])
def check_nsfw():
    # Check if the request contains an image file
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    # Get the image file from the request
    image_file = request.files['image']

    # Check if the image file has a filename
    if image_file.filename == '':
        return jsonify({"error": "No selected image"}), 400

    # Save the image temporarily to the 'temp' directory
    temp_path = os.path.join('temp', image_file.filename)
    image_file.save(temp_path)

    # Predict the NSFW score of the image and round it to the nearest integer
    check = round(n2.predict_image(temp_path))

    # Remove the temporary image file
    os.remove(temp_path)

    # Determine the result based on the NSFW score
    result = 1 if check > 0 else 0

    # Return the result as a JSON response
    return jsonify({"nsfw": result})


# Run the Flask application
if __name__ == '__main__':
    # Create the 'temp' directory if it doesn't exist
    if not os.path.exists('temp'):
        os.makedirs('temp')
    # Start the Flask app in debug mode
    app.run(debug=True)