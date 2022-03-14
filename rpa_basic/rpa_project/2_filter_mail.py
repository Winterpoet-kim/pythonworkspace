from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

index = 1  # 순번
applicant_list = []

for msg in mailbox.fetch('(SENTSINCE 14-Mar-2022)'):
    if "파이썬 특강" in msg.subject:
        nickname, phone = msg.text.strip().split("/")
        print(f"순번 : {index} 닉네임 : {nickname} 전화번호 : {phone}")
        applicant_list.append((msg, index, nickname, phone))
        index += 1

# for applicant in applicant_list:
#     print(applicant)

