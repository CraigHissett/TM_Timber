# sms.py
# Sends sms message to any cell phone using gmail smtp gateway
# Written by Alex Le

import smtplib

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com
# three:    number@three.co.uk
#           number@smtp-mbb.three.co.uk
# vodafone: number@vodafone.net
# ee:       number@mms.ee.co.uk

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login("user", 'pw' )

efrom = "Craigistan"
eto= ""
esubject= "DTT"
body = "Dusto Test Text"

message = ("From: %s\r\n" % efrom
         + "To: %s\r\n" % eto
         + "Subject: %s\r\n" % esubject
         + "\r\n"
         + body)


# Send text message through SMS gateway of destination number
server.sendmail(efrom, eto, message)
print('Sent Craig2')
