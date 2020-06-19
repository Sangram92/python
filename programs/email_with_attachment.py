import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
from os.path import basename

# credentials
receiver = 'patil.sangram01@gmail.com'
sender = 'XXXXXX@XXXXX.com'
password = 'XXXXXXXXXX'
subject = 'Email Subject'

# here you can pass attachment file location.
attachment = ''

mail_content = '''Hi,

This is a test email. Ignore it.


Thanks,
Sangram.
'''

try:
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender
	message['To'] = receiver
	message['Subject'] = subject
	message.attach(MIMEText(mail_content))

	if attachment:
		with open(attachment, "rb") as file_:
			part = MIMEApplication(
				file_.read(),
				Name=basename(attachment)
			)
		encoders.encode_base64(part)
		part['Content-Disposition'] = 'attachment; filename="%s"' % basename(attachment)
		message.attach(part)

	#Create SMTP session for sending the mail

	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo()
	session.starttls()
	session.login(sender, password)

	session.sendmail(sender, receiver, message.as_string())
	session.quit()
	print("Mail Sent Successfully.")
except Exception as e:
	print("Something went wrong {}".format(str(e)))