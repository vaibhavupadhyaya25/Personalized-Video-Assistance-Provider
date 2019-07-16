import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_it(email_send):
       cwd = os.getcwd()  # Get the current working directory (cwd)
       files = os.listdir(cwd)  # Get all the files in that directory
       print("Files in '%s': %s" % (cwd, files))


       email_user = 'bleedingbucky6@gmail.com'
       subject = 'yeh gya subject!'

       msg = MIMEMultipart()
       msg['From'] = email_user
       msg['To'] = email_send
       msg['Subject'] = subject

       body = 'ye gya message!'
       msg.attach(MIMEText(body,'plain'))

       filename = 'C:/Users/india/AppData/Local/Programs/Python/Python37/hashtag_list.csv'
       attachment = open(filename,'rb')

#-------------------------------------
       filename1 = 'C:/Users/india/AppData/Local/Programs/Python/Python37/RedditRealtimeDat.csv'
       filename2 = 'C:/Users/india/AppData/Local/Programs/Python/Python37/email_report.txt'
#------------------------------------

       part = MIMEBase('application','octet-stream')
       part.set_payload((attachment).read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition',"attachment; filename= "+filename)

       msg.attach(part)

#---------------------------------------------
       attachment = open(filename1,'rb')
       part = MIMEBase('application','octet-stream')
       part.set_payload((attachment).read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition',"attachment; filename= "+filename1)

       msg.attach(part)

       attachment = open(filename2,'rb')
       part = MIMEBase('application','octet-stream')
       part.set_payload((attachment).read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition',"attachment; filename= "+filename2)

       msg.attach(part)
#---------------------------------------------

       text = msg.as_string()

       server = smtplib.SMTP('smtp.gmail.com',587)
       server.starttls()
       server.login(email_user,'dhlptx@4new')


       server.sendmail(email_user, email_send,text)
       server.quit()
       print("Mail Successfully sent...")
