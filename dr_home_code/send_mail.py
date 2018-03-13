from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


try :
	pname=input("Enter the name of the person : ")
	print("Running by default email ids......")
	recipients = ['ksudhakar814@gmail.com'] 
	emaillist = [elem.strip().split(',') for elem in recipients]
	msg = MIMEMultipart()
	msg['Subject'] = str("medical suggestion")
	msg['From'] = 'shauryakhurana809@gmail.com'
	msg['Reply-to'] = 'ksudhakar814@gmail.com'
	 
	msg.preamble = 'Multipart message.\n'
	 
	part = MIMEText("Hi, please find the attached file for the attachment of the analysis by graphs")
	msg.attach(part)
	 
	part = MIMEApplication(open(str(pname+".png"),"rb").read())
	part.add_header('Content-Disposition', 'attachment', filename=str(pname+".png"))
	msg.attach(part)

	part = MIMEApplication(open(str(pname+"_suggestion.txt"),"rb").read())
	part.add_header('Content-Disposition', 'attachment', filename=str(pname+"_suggestion.txt"))
	msg.attach(part)
	 

	server = smtplib.SMTP("smtp.gmail.com:587")
	server.ehlo()
	server.starttls()
	server.login("shauryakhurana809@gmail.com", "******")
	 
	server.sendmail("shauryakhurana809@gmail.com", emaillist , msg.as_string())
except:
	print("*****Network problem******\n")
else :  
	print("Sent successfully")
