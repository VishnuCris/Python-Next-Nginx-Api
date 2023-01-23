from Models.Student import Student
from flask import jsonify
from db import db

def create_student_view(data):
	student = Student(firstname=data.get('FirstName'),lastname=data.get('LastName'),email=data.get('Email'),age=data.get('Age'),bio=data.get('Bio'))
	db.session.add(student)
	db.session.commit()
	return "Created Successfully"

def get_students_view():
	students = Student.query.all()
	studentArr = []
	if students:
		for student in students:
			studentList={}
			studentList['firstname'] = student.firstname
			studentList['lastname'] = student.lastname
			studentList['email'] = student.email
			studentList['age'] = student.age
			studentList['bio'] = student.bio
			studentList['id'] = student.id
			studentArr.append(studentList)
	return studentArr,True

def update_student_view(data):
	student = Student.query.get(data.get('id'))
	if not student:
		return 'No Student available under given id',False

	student.firstname = data.get('firstname')
	student.lastname = data.get('lastname')
	student.email = data.get('email')
	student.age = data.get('age')
	student.bio = data.get('bio')
	db.session.add(student)
	db.session.commit()
	return 'Updated successfully',True

def delete_student_view(data):
	student = Student.query.filter(Student.id == data.get('id'))
	if not student:
		return 'No Student available under given id',False

	student.delete()
	# db.session.add(student)
	db.session.commit()
	return 'deleted successfully',True

def checkStudentExist(data):
	student = Student.query.filter(Student.email == data.get('Emal')).first()
	if student:
		return 'Student already exists',False
	return '',True