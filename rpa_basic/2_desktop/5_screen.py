import pyautogui

# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")  # 파일로 저장

#pyautogui.mouseInfo()
#18,16 78,124,186 #4E7CBA

pixel = pyautogui.pixel(18,16)
print(pixel)

print(pyautogui.pixelMatchesColor(18,16,(79,125,187)))
print(pyautogui.pixelMatchesColor(18,16,pixel))