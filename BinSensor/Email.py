def SendEmail(recipient, subject, body):
    import smtplib
    import sys
    #sys.path. insert (0, 'Add\\windows path alternative')
    sys.path.insert(0, '/home/pi')
    import credentials

    gmail_user = credentials.GetUserEmail()
    gmail_pwd = credentials.GetUserPW()
    FROM = credentials.GetUser()
    #TO = recipient if type(recipient) is list else [recipient]
    TO = credentials.GetClientAdd()
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")
