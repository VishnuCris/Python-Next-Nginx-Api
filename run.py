# from app import app
from Python_Next_Nginx_Api import app
from waitress import serve

if __name__ == '__main__':
	if app.config['ENV'] == 'production':
		serve(app,host='127.0.0.1',port=5001)
	else:
		app.run(debug=True,port=5001)