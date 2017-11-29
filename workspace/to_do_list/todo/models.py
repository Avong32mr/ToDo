#from _future_ import unicode_literals
from datetime import datetime

from django.db import models

# import smtplib
# import sys

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title


# mail_username='ephraimavong32@gmail.com'
# mail_password='08133464782'
# from_addr = mail_username
# to_addrs=('ephraimavong32@gmail.com')
#
# HOST = 'smtp.gmail.com'
# PORT = 25
#
# # Create SMTP Object
# smtp = smtplib.SMTP()
# print 'connecting ...'
#
# # show the debug log
# smtp.set_debuglevel(1)
#
# # connet
# try:
#     print smtp.connect(HOST,PORT)
# except:
#     print 'CONNECT ERROR ****'
# # gmail uses ssl
# smtp.starttls()
# # login with username & password
# try:
#     print 'loginning ...'
#     smtp.login(mail_username,mail_password)
# except:
#     print 'LOGIN ERROR ****'
# # fill content with MIMEText's object
# msg =
# msg['From'] = from_addr
# msg['To'] = ';'.join(to_addrs)
# msg['Subject']='this is test msg'
# print msg.as_string()
# smtp.sendmail(from_addr,to_addrs,msg.as_string())
# smtp.quit()
