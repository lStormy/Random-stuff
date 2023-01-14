import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com',587)

smtp_obj.ehlo()
smtp_obj.starttls()

import getpass

email = input("Input your email: ")
password = getpass.getpass('Input your password: ')
smtp_obj.login (email,password)
print(smtp_obj.login(email,password))

from_adress = email
to_adress = input ('Input the email adress you want to send it to: ')

subject = input ('Enter the subject line: ')
message = input ('Enter the body message: ')
msg = 'Subject: ' + subject + '\n' + message

smtp_obj.sendmail(from_adress, to_adress, msg)