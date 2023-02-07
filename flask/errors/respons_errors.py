from flask import jsonify


def id_validation(parameter, value):
    parameter = int(parameter)
    if 0 >= parameter:
        return jsonify({"error": "Not Found. The user ID is lower or equal 0"}), 404
    elif parameter > 100:
        return jsonify({"error": "Not Found. The user ID is higher than 100"}), 404
    else:
        return jsonify(value), 200


def error_404():
    return jsonify({"error": "You provide invalid ID"}), 404


def error_500():
    return jsonify({"error": "Something went wrong, check the URL, Please check the ID"}), 500
