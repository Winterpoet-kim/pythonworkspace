from imap_tools import MailBox
from account import *
import smtplib
from email.message import EmailMessage
from openpyxl import Workbook


mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")


print("[1. 지원자 메일 조회]")
index = 1  # 순번
applicant_list = []
max_value = 3 # 최대 선정자수

for msg in mailbox.fetch('(SENTSINCE 14-Mar-2022)'):
    if "파이썬 특강" in msg.subject:
        nickname, phone = msg.text.strip().split("/")
        #print(f"순번 : {index} 닉네임 : {nickname} 전화번호 : {phone}")
        applicant_list.append((msg, index, nickname, phone))
        index += 1


print("[2. 선정 / 탈락 메일 발송]")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_addr = applicant[0].from_   # 수신 메일주소
        # index = applicant[1]
        # nickname = applicant[2]
        # phone = applicant[3]
        index, nickname, phone = applicant[1:]

        title = None
        content = None

        if index <= max_value:
            title = "[선정 안내 메일]"
            content = f"{nickname}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {index}번)"
        else:            
            title = "[탈락 안내 메일]"
            content = f"{nickname}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다.(대기순번 {index-max_value}번)"

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(f"{nickname}님에게 메일 발송 완료")

print("[3. 선정자 명단 파일 생성]")

wb = Workbook()
ws = wb.active

ws.append(["순번", "닉네임", "전화번호"])

for applicant in applicant_list[:max_value]:
    ws.append(applicant[1:])

wb.save("result.xlsx")
print("모든 작업이 완료되었습니다.")