import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "promodh2003@gmail.com"
password = "ljyaiqylvwibwkbs"

receiver = "promodh2003@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Check mail!
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
