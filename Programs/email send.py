import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "9060826518ng@gmail.com"  # Enter your address
receiver_email = "bi50_t.i.ivushkin@gmpt.ru"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: tixon

RUINER"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for i in range(0,3):
        server.sendmail(sender_email, receiver_email, message)
        print("Send!")
