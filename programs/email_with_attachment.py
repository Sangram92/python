import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email import encoders
from os.path import basename

# credentials
sender = 'patil.sangram01@gmail.com'
receiver = 'patil.sangram01@gmail.com'
password = ''

# here you can pass attachment file location.
attachment = ''

subject = 'Email Subject'
mail_content = '''
	Hi,

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
		# image attachment
		if attachment.split(".")[-1].lower() in ['jpg', 'png', 'jpeg']:
			img_data = open(attachment, 'rb').read()
			image = MIMEImage(img_data, name=os.path.basename(attachment))
			message.attach(image)
		else:
			with open(attachment, "rb") as file_:
				part = MIMEApplication(
					file_.read(),
					Name=basename(attachment)
				)
			encoders.encode_base64(part)
			part['Content-Disposition'] = 'attachment; filename="%s"' % basename(attachment)
			message.attach(part)

	# take user password
	if not password:
		password = raw_input("Please enter password here ... ")

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