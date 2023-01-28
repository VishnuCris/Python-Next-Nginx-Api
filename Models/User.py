from flask import current_app as app
from Python_Next_Nginx_Api.db import db
from sqlalchemy.sql import func

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(30),nullable=False)
    phone_number= db.Column(db.String(10),nullable=False)
    password= db.Column(db.String(100),nullable=False)
    Address1= db.Column(db.String(50),nullable=False)
    Address2= db.Column(db.String(50),nullable=False)
    pincode= db.Column(db.String(10),nullable=False)
    email= db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'