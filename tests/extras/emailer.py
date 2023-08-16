import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tests import methods

file_path = "/tests/testData/email.properties"
fromaddr = methods.get_data(file_path, 'details', 'sender_address')
toaddr = methods.get_data(file_path, 'details', 'receiver_address')

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = methods.get_data(file_path, 'details', 'subject')

# string to store the body of the mail
body = methods.get_data(file_path, 'details', 'mail_content')

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = methods.get_data(file_path, 'details', 'file_name')
attachment_path = methods.get_data(file_path, 'details', 'file_attachment_path')
attachment = open(attachment_path, "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp-mail.outlook.com', 587)

# start TLS for security
s.starttls()

# Authentication
sender_pass = methods.get_data(file_path, 'details', 'sender_pass')
s.login(fromaddr, sender_pass)

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
