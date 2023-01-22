from .routes import routes
from Views.students import (
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
# @avoidDuplicateEntry
def create_student():
	try:
		response = create_student_view(request.get_json())
		return jsonify({'msg':response,'status':True})
	except Exception as e:
		return jsonify({'msg':str(e),'status':False})

@routes.post('/list/student')
# @jwt_required()
def get_students():
	try:
		response,status = get_students_view()
		return jsonify({'data':response,'status':status})
	except Exception as e:
		return jsonify({'msg':str(e),'status':False})

@routes.post('/update/student')
def update_student():
	try:
		response,status = update_student_view(request.get_json())
		return jsonify({'msg':response,'status':status})
	except Exception as e:
		return jsonify({'msg':str(e),'status':False})

@routes.post('/delete/student')
def delete_student():
	try:
		response,status = delete_student_view(request.get_json())
		return jsonify({'msg':response,'status':status})
	except Exception as e:
		return jsonify({'msg':str(e),'status':False})