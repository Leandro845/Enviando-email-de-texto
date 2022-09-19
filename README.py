# Enviando-email-de-texto
Enviando email de texto com python/Sending text email with python   
#This is a text email send code using python

from email.message import EmailMessage
import smtplib


email = 'source email'
password = 'password'

#Head
msg = EmailMessage()
msg['From'] = email #Source email
msg['to'] = 'destination email' #Destinatiion email
msg['Subject'] = '...' #Email title
msg.set_content('...') #Text


with smtplib.SMTP_SSL('smtp.gmail.com', port=467) as smtp:
    smtp.login(email, password) #Login
    smtp.send_message(msg) #Send email
