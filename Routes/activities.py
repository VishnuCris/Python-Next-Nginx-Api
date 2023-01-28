from .routes import routes
from flask import jsonify,request
from flask_jwt_extended import jwt_required
from functools import wraps
from Views.activities import send_mail_view

@routes.get('/send_mail')
def send_mail():
	try:
		response = send_mail_view()
		return {'msg':response.get('message'),'status':response.get('status')}
	except Exception as Err:
		return {'msg':str(Err),'status':False}