from tkinter import *

root = Tk()
root.title("Dalbit GUI")
root.geometry("640x480")  # 가로 * 세로

txt = Text(root, width=30, height=5)  # 여러줄에 걸쳐서 입력 받을때 씀.
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)  # 한줄로 입력받을때 씀.
e.pack()
e.insert(0, "한 줄만 입력해요.") # 현재는 값이 비어있으므로 END를 써도 동일함.

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1=첫번째 라인 . 0=0번째 column  END=끝까지
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()



