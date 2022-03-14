import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."  # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "dalbit1983@naver.com" # 받는 사람

# 여러명에게 메일을 보낼때
#msg["To"] = "dalbit1984@naver.com", "dalbit1985@naver.com"

# 참조
#msg["Cc"] = "dalbit1984@naver.com", "dalbit1985@naver.com"

# 비밀참조
#msg["Bcc"] = "dalbit1984@naver.com", "dalbit1985@naver.com"

msg.set_content("테스트 본문입니다.")  # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

