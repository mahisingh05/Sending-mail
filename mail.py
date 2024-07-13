#gmail using python
import smtplib
from email.mime.text import MIMEText
sender_email = "mahisingh31.5.2003@gmail.com"
receiver_email = "akilatri123@gmail.com"
password = "mahi@123"

message ['From']  = sender_email
message ['To'] = receiver_email
message ['subject'] = 'Test Email from python' 

body = 'This is a test email sent from Python!'

try:
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Use 587 for TLS
    session.starttls()  # Enable security
    session.login(sender_email, password)  # Login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print('Mail Sent')
except Exception as e:
    print(f"Failed to send email: {e}")                         
