import tkinter.ttk as ttk
from tkinter import *  # __all__ 부분에 정의해주지 않으면 그 서브모듈에 대해서는 쓸수없으므로
from tkinter import filedialog  # 정의되지 않은 서브 모듈이므로 명시적으로 import를 해주어야함.
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("Image Integration")

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), initialdir=r"C:")

    # 사용자가 선택한 파일 목록
    for file in files:
        #print(file)
        list_file.insert(END, file)

# 파일 삭제
def del_file():
    # 사용자가 현재 리스트에서 선택한 파일 목록
    #print(list_file.curselection()) # 리스트에서 현재 선택된 인덱스 값 반환

    for index in reversed(list_file.curselection()):  # 뒤의 값부터 가져와서 for문 실행
        list_file.delete(index)


# 저장 경로 (폴더)
def save_path():
    s_path = filedialog.askdirectory()
    if s_path == "" :  # 사용자가 취소를 누를때
        return 
    #print(s_path)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, s_path)


# 이미지 통합
def  merge_image():
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    try:
        # 가로 넓이
        img_width = cmb_width.get()
        if img_width =="원본유지":
            img_width = -1  # -1 일때는 원본 기준으로 merge
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else :  # 없음
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower()  # PNG, JPG, BMP 값을 받아서 소문자로 변경

        ###############################################################
        

        #print(list_file.get(0, END))
        images = [Image.open(x) for x in list_file.get(0,END)]
        # size -> size[0] : width, size[1] : height
        # widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images]

        # 이미지 사이즈를 리스트에 넣어서 하나씩 처리
        image_sizes = []   # [(width1, height1), (width2, height2), ...]
        if img_width > -1 :
            image_sizes = [( int(img_width), int(img_width*x.size[1] / x.size[0]) ) for x in images]  # width 값 변경
        else :
            image_sizes = [(x.size[0], x.size[1]) for x in images] # 원본 사이즈 사용


        

        widths, heights = zip(*(image_sizes))
        
        max_width, total_height = max(widths), sum(heights)
        # print("max width : ", max_width)
        # print("total_height : ", total_height)

        # 스케치북 준비
        # 이미지 간격 옵션 적용
        if img_space > 0:
            total_height += (img_space*(len(images)-1))

        result_imgae = Image.new("RGB", (max_width, total_height),(255,255,255))
        y_offset = 0  # y 위치 정보
        # for img in images:
        #     result_imgae.paste(img, (0, y_offset))
        #     y_offset += img.size[1]  # height 값 만큼 더해줌.

        for idx, img in enumerate(images):
            # width 가 "원본유지"가 아닐때에는 이미지 크기를 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])
                
            
            result_imgae.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)   # height 값 + 간격(space)

            progress = (idx+1)/len(images)*100  # 실제 percent 정보를 계산
            p_var.set(progress)
            progress_bar.update()


        # 포맷 옵션 처리
        file_name = "Dalbit_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_imgae.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err:  # 예외처리
        msgbox.showerror("에러", err)

# 시작
def start():
    # 파일 목록 확인
    if list_file.size() == 0 :
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장경로를 선택하세요")
        return

    # 각 옵션들 값을 확인
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    # 이미지 통합 작업
    merge_image()
    


# 파일 프레임(파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # 프레임의 가로를 가득 채우기 / 간격 띄우기

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_delete_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_delete_file.pack(side="right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)  # ipady = 안쪽 여백->높아지는 효과

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=save_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 1-1. 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)
# 1-2. 가로 넓이 콤보박스
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 2-1. 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)
# 2-2. 간격 옵션 콤보박스
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 3-1. 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)
# 3-2. 파일 포맷 옵션 콤보박스
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# 진행 상황 progressbar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)



root.resizable(False, False)  # x(너비) y(너비) 값 변경불가 (창 크기 변경 불가)
root.mainloop()

