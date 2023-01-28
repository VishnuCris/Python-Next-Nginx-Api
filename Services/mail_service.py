from Python_Next_Nginx_Api import app
from flask_mail import Message,Mail

class MailService:
	def __init__(self):
		self.mail = Mail(app)

	def Send_Mail(self,mail_credentials):
		try:
			msg = Message(
	                mail_credentials.get('subject','Hello Ghosts'),
	                sender =app.config['MAIL_USERNAME'],
	                recipients =mail_credentials.get('reciptent',[]),
	                cc =mail_credentials.get('cc',[]),
	               )
			msg.body = mail_credentials.get('message','Ready to Rule')
			print(msg)
			print('msg')
			self.mail.send(msg)
			return {'status':True,'msg':'Mail Send Successfully'}
		except Exception as Err:
			print(Err)
			return {'status':False,'msg':str(Err)}




