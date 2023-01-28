import os
from flask import Flask, render_template, request, url_for, redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
import secrets
from sqlalchemy.sql import func
from datetime import timedelta
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
 	create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
import werkzeug


app = Flask(__name__)
# app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://vishnu:Password123#$!@localhost/AI_Coder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_COOKIE_SAMESITE'] = "None" 
app.config['JWT_COOKIE_SECURE']=True
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_COOKIE_DOMAIN'] = '127.0.0.1'
app.config['JWT_CSRF_IN_COOKIES'] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config['JWT_SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae4725f' 

jwt = JWTManager(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'effectivecoder717@gmail.com'
app.config['MAIL_PASSWORD'] = 'rmzuaxlpfktcezoy'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

CORS(app,support_credentials=True)

from .Routes.routes import routes
app.register_blueprint(routes,url_prefix='/api')

@app.after_request
def after_request(response):
    print('Request-Response Cycle Completed')
    # print(response.status_code)
    # print(response.get_json())
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Orgin'] = '*'
    return response
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    print(e)
    return {'msg':str(e)}

app.register_error_handler(401, handle_bad_request)