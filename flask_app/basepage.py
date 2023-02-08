import random
import time

from flask import Flask, jsonify, render_template, request
import logging
from data_for_response import planet, cosmo_boat, person
from respons_errors import id_validation, error_404

app = Flask(__name__, template_folder='templates')


@app.errorhandler(404)
def not_found():
    return error_404()

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Something went wrong, check the URL, Please check the ID'}), 500


@app.before_request
def log_request():
    logging.basicConfig(filename='requests.log', level=logging.INFO)
    logging.info(f'Request: {request.method} {request.url}')


@app.after_request
def log_response(response):
    logging.info(f'Response: {response.status}')
    return response


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/people/<parameter>/")
def people(parameter):
    if parameter.isdigit() or int(parameter) < 0:
        return id_validation(parameter, person)

    else:
        return jsonify({"error": "Not Found. id must be int"}), 404


@app.route("/planets/<parameter>/")
def planets(parameter):
    if parameter.isdigit() or int(parameter) < 0:
        return id_validation(parameter, planet)
    else:
        return jsonify({"error": "Not Found. id must be int"}), 404


@app.route("/starships/<parameter>/")
def starships(parameter):
    time.sleep(random.uniform(0, 0.5))
    if parameter.isdigit() or int(parameter) < 0:
        return id_validation(parameter, cosmo_boat)
    else:
        return jsonify({"error": "Not Found. id must be int "}), 404


if __name__ == '__main__':
    app.run()