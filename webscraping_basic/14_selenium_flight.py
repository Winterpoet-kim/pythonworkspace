from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 27일, 28일 선택
# browser.find_element_by_link_text("27")[0].click()  # [0] -> 이번달
# browser.find_element_by_link_text("28")[0].click()  # [0] -> 이번달


# 로딩 시간 처리 방법
# 1. 시간 간격을 두기. 예) time.sleep()
# 2. 필요한 element가 나올때까지만 기다리는 방법

# 10초 동안 EC(예상되는 조건)에따라 명시한 xpath값에 해당하는 element가 위치할때까지 기다린다.
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "...")))  
    # 성공했을때 동작 수행 영역
finally:
    # 실패하면 바로 종료
    browser.quit()



