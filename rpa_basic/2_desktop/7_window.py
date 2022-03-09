import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (VSCode)
# print(fw.title)  # 창의 제목 정보
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)

# pyautogui.click(fw.left+25, fw.top+20)

# for w in pyautogui.getAllWindows():
#     print(w)
    

# for w in pyautogui.getWindowsWithTitle("제목 없음"):
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:
    w.activate()  # 활성화 (화면 맨 앞으로 가져옴)

if w.isMaximized == False:
    w.maximize()  # 화면 최대화

# if w.isMinimize == False:
#     w.minimize()  # 화면 최소화

w.restore()  # 화면 원복

w.close()  # 윈도우 닫기