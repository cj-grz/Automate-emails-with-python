
import os
import smtplib
import imghdr
from email.message import EmailMessage
import re

EMAIL_ADDRESS = 'email'
EMAIL_PASSWORD = 'password'

firstname = 'firstname'
lastname = 'lastname'


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	with open("test.txt") as fp:
		line = fp.readline()
		while(line):
			linesplit = re.split(r'\t+', line)
			print(linesplit[0] + " : " + linesplit[1])
			msg = EmailMessage()
			msg['Subject'] = 'Subject'
			msg['From'] = EMAIL_ADDRESS
			msg.set_content('Hello ')
                        msg['To'] = " "
		        line = fp.readline()		
			smtp.send_message(msg)
