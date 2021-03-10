############--------------M1
import smtplib
import os
email_add=os.environ.get('kraj6250@gmail.com')
email_pass=os.environ.get('pass')
#enable less secure app on google account
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_add,email_pass)
    subject="start giving interview"
    body="from next week"
    msg=f'subject: {subject}\n\n{body}'
    smtp.sendmail(email_add,'raj.raj92120@gmail.com',msg)

#########################-----------------------------Another way- m2--------------------------------------------
import smtplib
import os
from email.message import EmailMessage
import imghdr   ####### for imag attaching to email
email_add=os.environ.get('kraj6250@gmail.com')
email_pass=os.environ.get('pass')
contacts=['abcde@gmail.com','xyz@gmail.com']
msg=EmailMessage()
msg['subject']="start giving interview"
msg['From']=email_add
msg['To']=','.join(contacts)
msg.set_content("from next week")
files=['pic1.jpg','pic2.jpg','pic3,jpg']   #attachments
for file1 in files:
    with open(file1,'rb') as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)
        file_name=f.name
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
    # msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name) for pdf attachment
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:  # sending email
    smtp.login(email_add, email_pass)
    smtp.send_message(msg)



#---------------html send---------------
import smtplib
import os
from email.message import EmailMessage
import imghdr   ####### for imag attaching to email
email_add=os.environ.get('kraj6250@gmail.com')
email_pass=os.environ.get('pass')
contacts=['abcde@gmail.com','xyz@gmail.com']
msg=EmailMessage()
msg['subject']="start giving interview"
msg['From']=email_add
msg['To']=','.join(contacts)
msg.set_content("from next week")
msg.add_alternative("""\<!Doctype html>
<h1>let me go
<html>
""",subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:  # sending email
    smtp.login(email_add, email_pass)
    smtp.send_message(msg)
























