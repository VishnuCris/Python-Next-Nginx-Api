from Python_Next_Nginx_Api import app
from flask_mail import Message,Mail
from Python_Next_Nginx_Api.Services.mail_service import MailService
import time,math


def send_mail_view():
	mailCredentials = {}
	mailCredentials['subject'] = 'Massive Success'
	mailCredentials['reciptent'] = ['vishnu717185@gmail.com']
	# mailCredentials['cc'] = []
	mailCredentials['message'] = 'Starting Poin For Massive Success'
	mailService = MailService()
	response = mailService.Send_Mail(mailCredentials)
	return {'status':True,'msg':response.get('msg')}

def Create_Content_View(data):
	try:
		return {'content':'Is under Devolopement','status':True}
	except Exception as Err:
		return {'msg':str(Err),'status':False}
