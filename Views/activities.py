from Python_Next_Nginx_Api import app
from flask_mail import Message,Mail
from Python_Next_Nginx_Api.Services.mail_service import MailService

def send_mail_view():
	mailCredentials = {}
	mailCredentials['subject'] = 'Massive Success'
	mailCredentials['reciptent'] = ['vishnu717185@gmail.com']
	# mailCredentials['cc'] = []
	mailCredentials['message'] = 'Starting Poin For Massive Success'
	mailService = MailService()
	response = mailService.Send_Mail(mailCredentials)
	return {'status':True,'message':response.get('msg')}