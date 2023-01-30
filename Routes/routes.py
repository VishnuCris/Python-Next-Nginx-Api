from flask import (
	Blueprint,current_app as app,jsonify,request,g,session,make_response
)
from Python_Next_Nginx_Api.db import db
from Python_Next_Nginx_Api.Models.User import User
from functools import wraps
import Python_Next_Nginx_Api.Views.views as views
from flask_jwt_extended import (
	set_access_cookies,set_refresh_cookies,
	jwt_required,unset_jwt_cookies
)
routes = Blueprint('routes',__name__)
from .students import *
from .activities import *

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'x-access-tokens' in request.headers:
           token = request.headers['x-access-tokens']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
           current_user = Users.query.filter_by(public_id=data['public_id']).first()
       except:
           return jsonify({'message': 'token is invalid'})
 
       return f(current_user, *args, **kwargs)
   return decorator

@routes.post('/login')
# @user_exist
def user_login():
	resp = views.isUserAvailable(request.get_json())
	auth = request.authorization  
	if resp:
		response= views.user_login(resp)
		return response
	return jsonify({'msg':'Not Registered with us !!!','status':False})	


@routes.post('/signup')
# @user_exist
def user_signup():
	resp = views.isUserAvailable(request.get_json())
	if resp:
		return jsonify({'msg':'Already Registered','status':False})
	response = views.user_signup(request.get_json())
	return response

@routes.post('/logout')
def user_logout():
	res = make_response({'msg':'logged out successfully','status':True	})
	unset_jwt_cookies(res)
	return res




