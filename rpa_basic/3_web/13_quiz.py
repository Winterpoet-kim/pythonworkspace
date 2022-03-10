import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/')

browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
browser.find_element_by_link_text('HOW TO').click()
browser.find_element_by_link_text('Contact Form').click()

first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

elem_fname = browser.find_element_by_id('fname').send_keys(first_name)

elem_lname = browser.find_element_by_id('lname').send_keys(last_name)

#browser.find_element_by_xpath('//*[@id="country"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()

elem_text = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)

browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)

# browser.close() # 현재 탭만 닫음
browser.quit()