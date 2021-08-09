#!venv/bin/python3

import os
import sys
import shlex
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()
args = sys.argv[1:]
print(args)

email = 'xeno25502@gmail.com'
target_email = args.pop(0)
password = os.getenv('PASSWORD')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

server.login(email, password)

msg = MIMEMultipart()
msg['From'] = 'AsyncXeno'
msg['To'] = target_email
msg['Subject'] = args.pop(0)
msg.attach(MIMEText(args.pop(0))) 

text = msg.as_string()
server.sendmail(email, target_email, text)
server.quit()
