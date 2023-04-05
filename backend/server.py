from flask import Flask, jsonify, request, send_from_directory, make_response, send_file
from flask_cors import CORS, cross_origin
from utils import *
from mistic import mistic
import os
import shutil
from io import BytesIO
import zipfile
from glob import glob
from waitress import serve
import codecs

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def home():
    return "Server is running"


@app.route('/getOutputs', methods=['GET'])
@cross_origin()
def get_outputs():
    return send_file(os.path.join(os.getcwd(), 'outputs.zip'), as_attachment=True)


@app.route('/mistic', methods=['POST'])
@cross_origin()
def run_mistic():
    print("Received request")
    # shutil.rmtree(UPLOAD_FOLDER)
    # shutil.rmtree(OUTPUT_FOLDER)
    # os.remove('outputs.zip')

    # os.makedirs(UPLOAD_FOLDER)
    # os.makedirs(OUTPUT_FOLDER)

    # data = request.form.to_dict()
    # if 'file' not in request.files:
    #     return "No shapefile found"
    # file = request.files['file']

    # if file.filename == '':
    #     return "No selected file"
    # if file and allowed_file(file.filename):
    #     file_names = unzip(file, UPLOAD_FOLDER)
    # shp_file = [f for f in file_names if f.endswith(".shp")]
    # if (len(shp_file) == 0):
    #     return "SHP file not found"
    # mistic(os.path.join(UPLOAD_FOLDER,
    #        shp_file[0]), OUTPUT_FOLDER, int(data['outputProj']), int(data['startYear']), int(data['endYear']), data['type'])
    # shutil.make_archive(os.path.join(
    #     os.getcwd(), 'outputs'), 'zip', OUTPUT_FOLDER)
    return jsonify({'results': get_images()})


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000, threads=1)
