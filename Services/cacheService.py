
from flask_restful import Api,Resource
from flask import jsonify

class CacheService(Resource):
	def get(self):
		return jsonify({'status':True,'msg':'From Cache'})