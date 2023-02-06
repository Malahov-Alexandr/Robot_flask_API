from flask import Flask, jsonify, render_template, request
import logging
from data.data_for_response import planet, cosmo_boat, person
from errors.respons_errors import id_validation, error_404

app = Flask(__name__, template_folder='templates')


@app.errorhandler(404)
def page_not_found():
    return error_404()


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


@app.route("/people/<int:parameter>/")
def people(parameter):
    if not isinstance(parameter, int):
        return jsonify({"error": f"{parameter} Not Found. id must be int"}), 404
    return id_validation(parameter, person)


@app.route("/planets/<int:parameter>/")
def planets(parameter):
    if not isinstance(parameter, int):
        return jsonify({"error": f"{parameter} Not Found. id must be int"}), 404
    return id_validation(parameter, planet)


@app.route("/starships/<int:parameter>/")
def starships(parameter):
    if not isinstance(parameter, int):
        return jsonify({"error": f"{parameter} Not Found. id must be int"}), 404
    return id_validation(parameter, cosmo_boat)


if __name__ == '__main__':
    app.run()
