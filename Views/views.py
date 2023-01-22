from Models.User import User
from Services.services import hashPassword
from werkzeug.security import generate_password_hash,check_password_hash
from db import db
from app import app
from flask import make_response
from flask_jwt_extended import create_access_token,create_refresh_token,set_refresh_cookies,set_access_cookies

def isUserAvailable(data):
	# userSQl = User.query.filter(User.email == data.get('email'),User.password == hashPassword(data.get('password')))
	userSQl = User.query.filter(User.email == data.get('email'))
	user = userSQl.first()
	if user:
		if check_password_hash(user.password,data.get('password')):
			return user
	return None

def user_signup(data):
	try:
		user = User(name=data.get('name'),password=hashPassword(data.get('password')),phone_number=data.get('mobile_number'),
			Address1=data.get('Address1'),Address2=data.get('Address2'),pincode=data.get('pincode'),email=data.get('email'))
		db.session.add(user)
		db.session.commit()
		access_token = create_access_token(identity=user.id)
		response = make_response({'msg':'Registered Succesfully','access_token':access_token,'status':True})
		set_access_cookies(response, access_token)
		return response
	except Exception as e:
		response = make_response({'msg':str(e),'status':False})
		return response

def user_login(data):
	try:
	   	user = data
	   	if user:
	   		access_token = create_access_token(identity=user.id)
	   		response = make_response({'msg':'Logined Succesfully','access_token':access_token,'status':True})
	   		set_access_cookies(response, access_token)
	   		return response,200
	   	else:
	   		response = make_response({'msg':'Not Registered with us !!!','status':False})
	   		return response
	except Exception as e:
		print(e)
		response = make_response({'msg':str(e),'status':False})
		return response



