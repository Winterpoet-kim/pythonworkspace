import pyautogui
#pyautogui.FAILSAFE = False  # 4모서리에 마우스를 옮겨도 중단되지 않게 옵션 설정(추천 안함)
#pyautogui.PAUSE = 1  # 모든 동작에 1초씩 sleep 적용


#pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100,100)
    pyautogui.sleep(1)
