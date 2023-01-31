from flask_restful import Api,Resource
from flask import jsonify
from Python_Next_Nginx_Api.Services.cacheService import CacheService

def addResources(app):
	api = Api(app)
	api.add_resource(CacheService, '/api/cache')

