from app.models.user import User
from app import response, db, app
from flask import request
from datetime import datetime
from datetime import timedelta
from flask_jwt_extended import *

def createAcc():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        status = request.form.get('status')

        users = User(
                    name=name, 
                    email=email, 
                    status=status
                )
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('Success', "Success input data")
    except Exception as err:
        return response.error('error', "error")

def singleObject(data):
    data={
        'id': data.id,
        'name': data.name,
        'email': data.email,
        'status': data.status,
    }
    return data

def loginAcc():
    try:
        email = request.json['email']
        password = request.json['password']

        users = User.query.filter_by(email=email).first()

        if not users:
            return response.error("Check Again", "Wrong Email or Password")
        
        if not users.checkPass(password):
            return response.error('Check Again', 'Wrong Email or Password')
        
        data=singleObject(users)

        expires = timedelta(hours=7)
        expires_refresh = timedelta(hours=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        
        return response.success({
            "userData": data,
            "active_token" : access_token,
            "refresh_token" : refresh_token,
        }, "Login Success")

    except Exception as err:
        print(err)
        return response.error('-', 'Data Not Found')