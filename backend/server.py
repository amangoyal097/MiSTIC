from flask import Flask, jsonify, request
from utils import *
from mistic import mistic
import os
from werkzeug.utils import secure_filename
import shutil


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Server is running"


@app.route('/mistic', methods=['POST'])
def run_mistic():
    shutil.rmtree(UPLOAD_FOLDER)
    shutil.rmtree(OUTPUT_FOLDER)
    os.makedirs(UPLOAD_FOLDER)
    os.makedirs(OUTPUT_FOLDER)
    data = request.form.to_dict()
    if 'file' not in request.files:
        return "No shapefile found"
    if "neighbors" not in request.files:
        return "No neighbors file found"
    file = request.files['file']

    neighbors = request.files['neighbors']

    neighbors_path = os.path.join(
        UPLOAD_FOLDER, secure_filename(neighbors.filename))
    neighbors.save(neighbors_path)

    if not check_csv(neighbors_path):
        return "Cannot parse csv file"

    if file.filename == '':
        return "No selected file"
    if file and allowed_file(file.filename):
        file_names = unzip(file, UPLOAD_FOLDER)
    shp_file = [f for f in file_names if f.endswith(".shp")]
    if (len(shp_file) == 0):
        return "SHP file not found"
    mistic(os.path.join(UPLOAD_FOLDER,
           shp_file[0]), OUTPUT_FOLDER, neighbors_path, int(data['startYear']), int(data['endYear']), data['type'])
    return "File received"
    # return jsonify({'result': get_images()})


if __name__ == '__main__':

    app.run(debug=True)
