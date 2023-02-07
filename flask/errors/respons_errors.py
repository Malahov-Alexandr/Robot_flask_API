from flask import jsonify


def id_validation(parameter, value):
    if not isinstance(parameter, int):
        return jsonify({"error": "Not Found. id must be int"}), 404
    elif 0 >= parameter and parameter < 100:
        return jsonify({"error": "Not Found. The user’s ID is lower or equal 0"}), 404
    elif parameter > 100:
        return jsonify({"error": "Not Found. The user’s ID is higher than 100"}), 404
    else:
        return jsonify(value)


def error_404():
    return jsonify({"error": "Not Found"}), 404