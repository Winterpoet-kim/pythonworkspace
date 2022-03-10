# import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")


# # level : debug < info < warning < error < critical
# # 설정 레벨보다 높은 단계의 로그만 찍는다.
# logging.debug("아 이거 누가 짠거야~~")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 조금 오래되었습니다. 문제가 있을 수 있습니다.")
# logging.error("에러가 발생하였습니다. 에러코드는...")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다.")


# 터미널과 파일에 함께 로그 남기기

import logging
from datetime import datetime

# 시간 [로그레벨] 메세지 형태로 로그를 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")  
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림 (터미널에 출력)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
filehandler = logging.FileHandler(filename, encoding="utf-8")
filehandler.setFormatter(logFormatter)
logger.addHandler(filehandler)

logger.debug("로그를 남기는 테스트를 진행합니다.")