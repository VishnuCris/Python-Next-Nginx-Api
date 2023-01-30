from .routes import routes
from Python_Next_Nginx_Api.Views.students import (
	get_students_view,create_student_view,update_student_view,
	checkStudentExist,delete_student_view
)
from flask import jsonify,request
from flask_jwt_extended import jwt_required
from functools import wraps

###Decorators###
def avoidDuplicateEntry(func):
	@wraps(func)
	def decorator():
		response,status = checkStudentExist(request.get_json())
		if not status:
			return jsonify({'msg':response,'status':status})
		return func()
	return decorator

@routes.post('/create/student')
@jwt_required()
def create_student():
	response = create_student_view(request.get_json())
	return jsonify({'msg':response,'status':True})

@routes.post('/list/student')
@jwt_required()
def get_students():
	response,status = get_students_view()
	return jsonify({'data':response,'status':status})

@routes.post('/update/student')
@jwt_required()
def update_student():
	response,status = update_student_view(request.get_json())
	return jsonify({'msg':response,'status':status})

@routes.post('/delete/student')
@jwt_required()
def delete_student():
	response,status = delete_student_view(request.get_json())
	return jsonify({'msg':response,'status':status})
