from app.models.project import Project
from app.models.client import Client
from app import response, db, app
from flask import request, jsonify
import math


def formatProject(datas):
    array = []
    
    for i in datas:
        array.append(singleProject(i))

    return array

def singleProject(data):
    data = {
        "project_name": data.project_name,
        "project_status": data.project_status,
        "project_start": data.project_start,
        "project_end": data.project_end,
        "client_id": data.client_id
}
    return data

def getAllProject():
    try:
        projects = Project.query.all()
        data = formatProject(projects)
        clients = Client.query.all()
        
        dataClients = formatClients(clients)
        return response.success({"projects":data, 'client':dataClients}, "Success")
    except Exception as err:
        print(err)
        return response.error('', "Error")
    
def detailIdProject(id):
    try:
        projects = Project.query.filter_by(project_id=id).first()
        clients = Client.query.filter(Client.client_id==id)

        print(Client.client_id==id)
        if not projects:
            return response.error([], 'Data not Found')
        
        dataClients = formatClients(clients)

        data = detailClients(projects, dataClients)
        return response.success(data, "Success") 

    except Exception as err:
        return print(err)


def detailClients(projects, client):
    data = {
        'project_name' : projects.project_name, 
        'project_start' : projects.project_start, 
        'project_end' : projects.project_end, 
        'project_status' : projects.project_status,
        'client' : client
    }
    
    return data

def singleClient(data):
    data = {
        'client_id': data.client_id,
        'client_name': data.client_name,
        'client_address': data.client_address
    }
    
    return data

def formatClients(data):
    array = []

    for i in data:
        array.append(singleClient(i))
    print(array, "array")
    return array


def postProject():
    try:
        project_name = request.json['project_name']
        project_start = request.json['project_start']
        project_end = request.json['project_end']
        project_status = request.json['project_status']
        client_id = request.json['client_id']

        projects = Project(
            project_name=project_name, 
            project_start=project_start, 
            project_end=project_end, 
            project_status=project_status,
            client_id=client_id
        )
        projectsPost = {
            'project_name': project_name, 
            'project_start': project_start, 
            'project_end': project_end, 
            'project_status': project_status,
            'client_id': client_id
        }
        print(project_name, "projectsPost")
        db.session.add(projects)
        db.session.commit()

        return response.success("Success", 'Success Create Data')
    except Exception as err:
        return response.error({"error": err}, "Can't Post This Time")

def deleteProject(id):
    try:
        projects = Project.query.filter_by(project_id=id).first()
        if not projects:
            return response.error([], 'Failed')

        db.session.delete(projects)
        db.session.commit()
        
        return response.success('', "Delete Success")
    except Exception as err:
        return err

def changeProject(id):
    try:
        project_name = request.json['project_name']
        project_start = request.json['project_start']
        project_end = request.json['project_end']
        project_status = request.json['project_status']
        client_id = request.json['client_id']

        input = [
            {
                'project_name': project_name,
                'project_start': project_start,
                'project_end': project_end,
                'project_status': project_status,
                'client_id': client_id
            }
        ]

        projects = Project.query.filter_by(project_id=id).first()

        projects.project_name= project_name
        projects.project_start=project_start
        projects.project_end=project_end
        projects.project_status=project_status
        projects.client_id=client_id

        db.session.commit()

        return response.success(input, "Update Success")
    except Exception as err:
        return response.error('Error', "Failed")
    
def paginationProject(clss, url, start, limit):
    try:
        result = clss.query.all()
        data = formatProject(result)
        print(result, "data")
        count = len(data)
        
        obj = {}
        
        if count < start:
            obj['Success'] = False
            obj['Message'] = 'No More Data to Display'
            return obj
        else:
            obj['Success'] = True
            obj['start_page'] = start
            obj['per_page'] = limit
            obj['total_data'] = count
            obj['total_page'] = math.ceil(count / limit)
            
            if start == 1:
                obj['Prev'] = ""
            else:
                start_copy = max(1, start - limit)
                
                limit_copy = start - 1
                
                obj['Prev'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
            if start + limit > count:
                obj['Next'] = ''
            else:
                start_copy = start + limit
                obj['Next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
            obj['result'] = data[(start-1) : (start - 1 + limit)]
            return obj
    except Exception as err:
        return response.error('Failed', "Failed Get Data")

def pagination():
    start = request.args.get('start')
    limit = request.args.get('limit')
    
    try:
        if start == None or limit == None:
            return jsonify(paginationProject(
                Project,
                'http://localhost:5000/pagination/project',
                start = request.args.get('start', 1),
                limit = request.args.get('limit', 5)
            ))
        else:
            return jsonify(paginationProject(
                Project,
                'http://localhost:5000/pagination/project',
                start = int(start),
                limit = int(limit)
            ))
            
    except Exception as err:
        return response.error('Error', "Error Get Pagination")

def searchProject():
    try:
        search = request.args.get('search')
        results= Project.query.filter(Project.project_name.like('%'+search+'%')).all
        print(search, "search")
        print(results, "results")
        if results == None:
            return response.error('-', "Failed Get Data")
        else:
            return None 
        
        # return response.success(results, "Success")
    except Exception as err:
        return response.error('Error', "Error")