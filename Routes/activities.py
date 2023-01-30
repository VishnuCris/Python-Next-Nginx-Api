from .routes import routes
from flask import jsonify,request
from flask_jwt_extended import jwt_required
from functools import wraps
from Python_Next_Nginx_Api.Views.activities import send_mail_view,Create_Content_View

@routes.get('/send_mail')
def send_mail():
	response = send_mail_view()
	return jsonify(response)


@routes.post('/AI_Content/create')
def Create_Content():
	response = Create_Content_View(request.get_json())
	return jsonify(response)

@routes.get('/exception_handling')
def exceptionHandling():
	# raise Exception('Testing')
	return jsonify({'status':True,'msg':'Success'})
	