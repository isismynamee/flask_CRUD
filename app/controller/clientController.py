from app.models.client import Client
from app import response, db, app
from flask import request

def getAllClient():
    try:
        clients = Client.query.all()
        data = formatClients(clients)

        return response.success(data, 'Success')
    except Exception as err:
        print(err)
        return response.error

def formatClients(datas):
    array = []
    for i in datas:
        array.append(singleClient(i))
    return array

def singleClient(data):
    data = {
        'client_name' : data.client_name,
        'client_address' : data.client_address
    }
    
    return data

# def detailClient(id):
#     try:
#         clients =  Client.query.filter_by(client_id=id).first()
#         data = formatClients(clients)
#         return jsonify(data)
#     except Exception as err:
#         print(err)
#         return response.error

def postClient():
    try:
        client_name = request.json['client_name']
        client_address = request.json['client_address']

        clients = Client(client_name=client_name, client_address=client_address)
        data = {
            'client_name':client_name, 
            'client_address':client_address
        }
        db.session.add(clients)
        db.session.commit()

        return response.success(data, 'Success Create Data')
    except Exception as err:
        return response.error('-', 'Failed')