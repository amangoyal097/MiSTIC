from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
from utils import *
from mistic import mistic
import os
import shutil
from waitress import serve
from coreRegion import core_analysis
import werkzeug.serving
import json
from zipfile import ZipFile

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
    try:
        shutil.rmtree(UPLOAD_FOLDER)
        shutil.rmtree(OUTPUT_FOLDER)
        os.remove('outputs.zip')
    except:
        pass

    os.makedirs(UPLOAD_FOLDER)
    os.makedirs(OUTPUT_FOLDER)

    data = request.form.to_dict()
    with open("config.json", "w") as f:
        json.dump(data, f)
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
           shp_file[0]), OUTPUT_FOLDER, int(data['outputProj']), int(data['startYear']), int(data['endYear']), data['type'])
    shutil.make_archive(os.path.join(
        os.getcwd(), 'outputs'), 'zip', OUTPUT_FOLDER)
    return jsonify({'results': get_images()})


@app.route('/coreAnalysis', methods=['POST'])
@cross_origin()
def run_core_analysis():
    print("Core request received")
    params = request.form.to_dict()
    with open("config.json", "r") as f:
        data = json.load(f)
    core_analysis(OUTPUT_FOLDER, int(data['startYear']),
                  int(data['endYear']), int(params['itf']), int(params['minSupport']), 3, 3, 3, 0, data)
    try:
        os.remove("coreOutputs.zip")
    except:
        pass
    with ZipFile('coreOutputs.zip', 'w') as zipObj:
        zipObj.write(
            OUTPUT_FOLDER + "/initial_ref_foci_{}.csv".format(params['itf']), "initial_ref_foci.csv")
        zipObj.write(OUTPUT_FOLDER +
                     "/ccInfo_{}.csv".format(params['minSupport']), "ccInfo.csv")
        zipObj.write(OUTPUT_FOLDER +
                     "/core_zone_influence_{}.csv".format(params['minSupport']), "core_zone_influence.csv")
    return "success"


@app.route('/getCoreOutputs', methods=['GET'])
@cross_origin()
def get_core_outputs():
    return send_file(os.path.join(os.getcwd(), 'coreOutputs.zip'), as_attachment=True)


def run_server():
    app.debug = True
    serve(app, host='0.0.0.0', port=5000, threads=1)


if __name__ == '__main__':
    run_server()
