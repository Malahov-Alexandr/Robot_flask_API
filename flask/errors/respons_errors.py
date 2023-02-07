from flask_app import jsonify


def id_validation(parameter, value):
    """This function validates the ID of the user.
    If the ID is lower or equal 0 or higher than 100, the function returns the error message.
    If the ID is correct, the function returns the value of the user.
    """
    parameter = int(parameter)
    if 0 >= parameter:
        return jsonify({"error": "Not Found. The user ID is lower or equal 0"}), 404
    elif parameter > 100:
        return jsonify({"error": "Not Found. The user ID is higher than 100"}), 404
    else:
        return jsonify(value), 200


def error_404():
    """This function returns the error message if the user provides invalid ID."""
    return jsonify({"error": "You provide invalid ID"}), 404


def error_500():
    """This function returns the error message if the user provides invalid URL."""
    return jsonify({"error": "Something went wrong, check the URL, Please check the ID"}), 500
