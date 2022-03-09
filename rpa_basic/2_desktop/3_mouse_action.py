import pyautogui

pyautogui.sleep(3)
#print(pyautogui.position())

#pyautogui.click(62, 8, duration=1)
#pyautogui.mouseDown()
#pyautogui.mouseUp()   # 2개 동작을 합치면 click(), drag&drop에 활용

#pyautogui.click(clicks=500)   # 500번 클릭

# pyautogui.moveTo(300,300)
# pyautogui.mouseDown()
# pyautogui.moveTo(500,500)
# pyautogui.mouseUp()

# pyautogui.rightClick()
# pyautogui.middleClick()

# pyautogui.moveTo(867, 150, duration=2)
# pyautogui.drag(100, 100, duration=2)  # 상대좌표 이동
# pyautogui.dragTo(100, 100, duration=2)  # 절대좌표 이동

pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤
# -300 : 아래 방향으로 300만큼 스크롤