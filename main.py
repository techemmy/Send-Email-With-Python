import smtplib, ssl
from getpass import getpass

sender_email = "emmanueltopea@gmail.com"
receiver_email = "xlfqpnindxett@candassociates.com"
sender_password = getpass(prompt='Enter your password: ')
port = 587
smtp_server = "smtp.gmail.com"
message = """\
Subject: New Message

Hello there."""

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
