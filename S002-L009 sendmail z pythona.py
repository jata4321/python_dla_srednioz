import smtplib

mailFrom = 'jata4321@w-web.pl'
mailTo = 'jakub.taborowicz@gmail.com'
mailSubject = 'Success 2!'
mailBody = 'This is mail body'

message = """From: Person 1 <{}>
To: Person 2 <{}>
Subject: {}

{}
""".format(mailFrom, mailTo, mailSubject, mailBody)

user = 'jata4321@w-web.pl'
password = 'Webmail12'
try:
    server = smtplib.SMTP_SSL('jata4321.atthost24.pl', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('Mail sent')
except BaseException:
    print('Failure sending mail!')
