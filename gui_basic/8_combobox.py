from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Dalbit GUI")
root.geometry("640x480")  # 가로 * 세로

values=[str(i)+"일" for i in range(1,32)] # 1 ~ 31까지의 숫자

combobox = ttk.Combobox(root, height=5, values=values)  # height = 한번에 보여지는 목록의 수
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")  # 읽기 전용
readonly_combobox.current(0)  # 0번째 인덱스 값 선택
readonly_combobox.pack()



def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()



