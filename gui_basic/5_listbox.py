from tkinter import *

root = Tk()
root.title("Dalbit GUI")
root.geometry("640x480")  # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "포도")
listbox.insert(END, "수박")
listbox.pack()

def btncmd():
    #listbox.delete(END)  # 맨뒤의 항목를 삭제
    #listbox.delete(0)  # 맨앞의 항목를 삭제

    # 갯수 확인
    #print("리스트에는 : ", listbox.size(), "개가 있습니다.")

    # 항목 확인 (시작 idx, 끝 idx)
    print("1번째에서 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인
    print("선택된 항목 : ", listbox.curselection())  # 선택된 항목의 index값 반환
    


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()



