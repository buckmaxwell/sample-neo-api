import os
from flask import Flask, jsonify, request
from user import User
import application_codes


app = Flask(__name__)
url = os.environ.get("NEO4J_REST_URL")


@app.route('/', methods=['GET'])
def index():
    """ Call this method for basic version info or to ensure the api is running. """
    return 'Your api is up and running!'


@app.route('/users/<id>', methods=['GET', 'PATCH', 'DELETE'])
@app.route('/users', defaults={'id': None}, methods=['POST', 'GET'])
def user(id):
    """Methods directly Related to the user resource"""
    response = None
    if request.method == 'POST':
        response = User.create_resource(eval(request.data))
    elif request.method == 'PATCH':
        response = User.update_resource(eval(request.data), id)
    elif request.method == 'DELETE':
        response = User.set_resource_inactive(id)
    elif request.method == 'GET':
        response = User.get_resource_or_collection(request.args, id)
    return response


@app.route('/users/<id>/relationships/<related_collection_name>/<related_resource>', methods=['GET', 'DELETE'])
@app.route('/users/<id>/relationships/<related_collection_name>', defaults={'related_resource': None}, methods=['GET', 'DELETE'])
def user_relationships(id, related_collection_name, related_resource):
    """Methods related to user relationships"""
    response = None
    if request.method == 'GET':
        response = User.get_relationship(request.args, id, related_collection_name, related_resource)
    elif request.method == 'DELETE':
        response = User.delete_relationship(id, related_collection_name, related_resource)
    return response


@app.route('/users/<id>/<related_collection_name>/<related_resource>', methods=['GET', 'DELETE'])
@app.route('/users/<id>/<related_collection_name>', defaults={'related_resource': None}, methods=['GET', 'DELETE'])
def user_related_resources(id, related_collection_name, related_resource):
    """Methods that return resources related to the user resource"""
    response = None
    if request.method == 'GET':
        response = User.get_related_resources(request.args, id, related_collection_name, related_resource)
    if request.method == 'DELETE':
        response = User.set_related_resources_inactive(id, related_collection_name, related_resource)
    return response


@app.errorhandler(404)
def not_found(error):
    """Return an error response for resources that don't exist"""
    return application_codes.error_response([application_codes.RESOURCE_NOT_FOUND])


@app.errorhandler(405)
def method_not_allowed(error):
    """Return an error response when requests supply an unsupported HTTP method"""
    return application_codes.error_response([application_codes.METHOD_NOT_ALLOWED])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10200, debug=True)


