import pyautogui

# 키보드에서 (window) + shift + S 키 동시에 누르기 (영역 캡쳐)

# 현재 화면에서 선택된 이미지를 찾아서 위치 정보 반환
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 이미지를 찾지 못했을때...  None 반환
# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 같은 이미지가 여러개 있을 경우
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)


# 처리 속도 개선
# 1. GrayScale : 속도 30%정도 개선, 정확도는 조금 떨어짐
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1700, 730, 200, 70))
# pyautogui.moveTo(trash_icon)

#pyautogui.mouseInfo()
#1700, 730
#1900, 800

# 3. 정확도 조정 (90% 정도만 맞아도 인식)
# run_btn = pyautogui.locateOnScreen("run_button.png", confidence=0.9)  
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notpad = pyautogui.locateOnScreen("file_menu_notepad.png")
# # if file_menu_notpad:
# #     pyautogui.click(file_menu_notpad)
# # else:
# #     print("발견 실패")

# while file_menu_notpad is None:
#     file_menu_notpad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notpad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

timeout = 10  # 10초 대기
start = time.time()  # 시작 시간 설정
file_menu_notpad = None
while file_menu_notpad is None:
    file_menu_notpad = pyautogui.locateOnScreen("file_menu_notepad.png")
    end = time.time()  # 종료 시간 설정
    if end-start > timeout:
        print("시간 종료")
        sys.exit()

pyautogui.click(file_menu_notpad)

