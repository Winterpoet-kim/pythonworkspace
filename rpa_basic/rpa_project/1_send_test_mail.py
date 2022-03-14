import smtplib
from account import *
from email.message import EmailMessage
from random import *

msg = EmailMessage()
msg["Subject"] = "파이썬 특강 신청합니다."  # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "ggamssi23@gmail.com" # 받는 사람

nicknames = ["유재석", "박명수", "정형돈", "노홍철", "조세호"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."  # 제목
        msg["From"] = EMAIL_ADDRESS # 보내는 사람
        msg["To"] = "ggamssi23@gmail.com" # 받는 사람
        msg.set_content(f"{nickname}/{str(randint(1000,9999))}")
        
        smtp.send_message(msg)
        print(nickname+"님으로부터 메일 수신 완료")
