#there will be an authentication error bcz of gmail security
#to use it properly u need to set an app password
#Go to myaccount.google.com/u/1/apppasswords
#and put app name = Python
#copy the app password and paste in the input password field




from email.message import EmailMessage
import ssl
import smtplib
import getpass

sender_email = input("Enter sender mail: ")
password = input('Enter APP-password: ')
reciever_email = input('Enter reciever mail: ')
mail_amount = int(input("number of mails to be sent: "))
subject = input('Enter subject/topic: ')
body = input('Enter content to be mailed: ')

em = EmailMessage()
em["From"] = sender_email
em['To'] = reciever_email
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()
i=0
while i<mail_amount:
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, reciever_email, em.as_string())
        i+=1
    except:
        print("Failed!")
        break
