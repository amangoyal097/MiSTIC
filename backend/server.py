from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from utils import *
from mistic import mistic
import os
import shutil


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def home():
    return "Server is running"


@app.route('/mistic', methods=['POST'])
@cross_origin()
def run_mistic():
    print("Received request")
    shutil.rmtree(UPLOAD_FOLDER)
    shutil.rmtree(OUTPUT_FOLDER)
    os.makedirs(UPLOAD_FOLDER)
    os.makedirs(OUTPUT_FOLDER)
    data = request.form.to_dict()
    if 'file' not in request.files:
        return "No shapefile found"
    file = request.files['file']

    if file.filename == '':
        return "No selected file"
    if file and allowed_file(file.filename):
        file_names = unzip(file, UPLOAD_FOLDER)
    shp_file = [f for f in file_names if f.endswith(".shp")]
    if (len(shp_file) == 0):
        return "SHP file not found"
    mistic(os.path.join(UPLOAD_FOLDER,
           shp_file[0]), OUTPUT_FOLDER, int(data['startYear']), int(data['endYear']), data['type'])
    return jsonify({'result': get_images()})


if __name__ == '__main__':

    app.run(debug=True)
