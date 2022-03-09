import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]    # 메모장 1개를 띄운 상태에서 가져옴.
print(w)
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=1)
# pyautogui.write("나도코딩")  # pyautogui 에서는 한글 입력 처리가 되지 않음.

# test 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번, la 적고 enter
# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# 구글 검색 : automate the boring stuff with python 챕터20 확인-> keyboard attribute 찾기(table20-1)
# 글자별로 의미가 무엇인지 확인가능

# 특수 문자
# shift 4  -> $
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")  # press("a")
# pyautogui.keyUp("ctrl") # -> Ctrl+A

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift","a")
# pyautogui.hotkey("ctrl","a")

import pyperclip

pyperclip.copy("나도코딩")  # 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v")