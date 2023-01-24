from flask import jsonify, make_response

def success(values, messages):
    res = {
        "data": values,
        "message": messages
    }

    return make_response(jsonify(res)), 200

def error(values, messages):
    res = {
        "data": values,
        "message": messages
    }

    return make_response(jsonify(res)), 400