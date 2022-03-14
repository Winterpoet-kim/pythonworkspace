from imap_tools import MailBox
from account import *

# with 를 쓰면 마지막에 mailbox.logout() 이 필요없음.
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True): # 전제 메일 다 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않은 메일만 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # for msg in mailbox.fetch('(FROM dalbit1983@naver.com)', limit=3): # 특정인이 보낸 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # for msg in mailbox.fetch('(TEXT "Security")', limit=5): # 어떤 글자를 포함하는 메일(제목, 본문)
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # for msg in mailbox.fetch('(SUBJECT "Google")', limit=5): # 어떤 글자를 포함하는 메일(제목만)
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 한글은 쿼리가 불가능
    # 우회 처리하는 방법
    # for msg in mailbox.fetch(limit=5, reverse=True): 
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SENTSINCE 10-Mar-2022)', reverse=True, limit=5): # 특정 날짜 이후의 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # for msg in mailbox.fetch('(ON 14-Mar-2022)', reverse=True, limit=5): # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건을 모두 만족하는 메일 검색 (AND조건)
    # for msg in mailbox.fetch('(ON 10-Mar-2022 SUBJECT "Google")', reverse=True, limit=5): # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))
        
    # 2가지 이상의 조건중 하나라도 만족하는 메일 검색 (OR조건)
    for msg in mailbox.fetch('(OR ON 10-Mar-2022 SUBJECT "Google")', reverse=True, limit=5): # 특정 날짜에 온 메일
        print("[{}] {}".format(msg.from_, msg.subject))