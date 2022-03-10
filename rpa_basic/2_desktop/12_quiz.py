import pyautogui
import sys
import pyperclip

# ----- My version ------
# pyautogui.hotkey("winleft","r")
# pyautogui.write("mspaint")
# pyautogui.click(170,990, duration=1)
# pyautogui.click(1660,120, duration=1)
# pyautogui.click(333,70, duration=1)

# pyautogui.mouseDown(45, 170)
# pyautogui.mouseUp(300, 300)

# pyperclip.copy("참 잘했어요")
# pyautogui.hotkey("ctrl", "v")
# #pyautogui.sleep(5)

# pyautogui.click(1846, 13, duration=1)
# pyautogui.click(1694, 127, duration=1)
# pyautogui.click(980, 545, duration=1)

#pyautogui.mouseInfo()

# ----- NadoCoding version ------

pyautogui.hotkey("winleft","r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(1)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if window.isMaximized == False:
    window.maximize()

pyautogui.sleep(1)

text_btn = pyautogui.locateOnScreen("text_btn.png")
if text_btn:
    pyautogui.click(text_btn)
else: 
    print("찾기 실패")
    sys.exit() 

pyautogui.mouseDown(45, 170)
pyautogui.mouseUp(300, 300)

pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")
pyautogui.sleep(2)

window.close()
pyautogui.sleep(1)
pyautogui.press("n")
