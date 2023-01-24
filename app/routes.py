from app import app, response
from app.controller import clientController, projectController, userController
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

@app.route('/auth-user', methods=['GET'])
@jwt_required
def auth():
    current_user = get_jwt_identity()
    print(current_user, "current User")
    return response.success(current_user, "Success")

@app.route('/search_project/<search>', methods=['POST', 'GET'])
def searching():
    return projectController.searchProject()

@app.route('/client', methods=['POST', 'GET'])
# @jwt_required()
def clients():
    if request.method == 'GET':
        return clientController.getAllClient()
    else:
        return clientController.postClient()


@app.route('/createacc', methods=['POST'])
# @jwt_required()
def create():
    return userController.createAcc()

@app.route('/login', methods=['POST'])
def login():
    return userController.loginAcc()

@app.route('/project', methods=['POST', 'GET'])
def project():
    if request.method == 'GET':
        return projectController.getAllProject()
    else:
        return projectController.postProject()

@app.route('/pagination/project', methods=['GET'])
def pagination():
    return projectController.pagination()

@app.route('/project/<id>', methods=['GET', 'DELETE', 'PATCH'])
# @jwt_required()
def detailProject(id):
    if request.method == 'GET':
        return projectController.detailIdProject(id)
    elif request.method == 'PUT':
        return projectController.changeProject(id)
    elif request.method == 'DELETE':
        return projectController.deleteProject(id)