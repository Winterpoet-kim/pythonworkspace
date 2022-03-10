#파일 기본
from datetime import datetime
import os
# print(os.getcwd())  # 현재 directory를 가져옴
# os.chdir("rpa_basic") 
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())
# os.chdir("c:/")
# print(os.getcwd())

# 파일 경로
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
#print(os.path.dirname(r"C:\Users\admin\Desktop\Code\pythonworkspace\my_file.txt"))


# 파일 정보 가져오기
import time
import datetime
# 1. 파일 생성 날짜
# ctime = os.path.getctime("run_button.png")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime))
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 2. 파일 수정 날짜
# mtime = os.path.getmtime("run_button.png")
# print(mtime)
# print(datetime.datetime.fromtimestamp(mtime))
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 3. 파일의 마지막 접근 날짜
# atime = os.path.getatime("run_button.png")
# print(datetime.datetime.fromtimestamp(atime))
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 4. 파일 크기
# size = os.path.getsize("run_button.png")
# print(size)  # 바이트 단위로 파일 크기 가져오기


# 파일 목록 가져오기
#print(os.listdir())  # 모든 폴더, 파일 목록 가져오기
#print(os.listdir("rpa_basic"))  # 주어진 폴더 밑의 모든 폴더, 파일 목록 가져오기

# 파일 목록 가져오기(하위 폴더 모두 포함)
# result = os.walk("rpa_basic")  # 주어진 폴더 밑의 모든 폴더, 파일 목록 가져오기
# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)


# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."): 
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)


# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
# import fnmatch
# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk("."): 
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)


# 주어진 경로가 파일인지 폴더인지 확인
# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic"))

# # 만약에 지정된 경로에 해당하는 파일/폴더가 없다면?
# print(os.path.isfile("run_buttooooonn.png"))

# 주어진 경로가 존재하는가?
# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")


# 파일 만들기
#open("new_file.txt","a").close()  # 빈파일 생성

# 파일명 변경하기
#os.rename("new_file.txt", "new_file_rename.txt")

# 파일 삭제하기
#os.remove("new_file_rename.txt")


# 폴더 만들기
#os.mkdir("new_folder")
#os.makedirs("new_folder/a/b/c")  # 하위 폴더를 가지는 폴더 생성

# 폴더명 변경하기
#os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
#os.rmdir("new_folder_rename")  # 폴더 안이 비었을때만 삭제 가능

import shutil  # shell utilities
# shutil.rmtree("new_folder_rename")  # 폴더 안이 비어있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될 수 있으므로 주의!!!

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_button.png", "test_folder")  # 원본 파일 경로, 대상 폴더경로
# shutil.copy("run_button.png", "test_folder/copied_run_button.png") # 원본 파일 경로, 대상 경로(변경된 파일명까지)

# shutil.copyfile("run_button.png", "test_folder/copied_run_button2.png")  # 원본 파일 경로, 대상 파일 경로

# # copy, copyfile : 메타정보 복사 X
# # copy2 : 메타정보 복사 O
# shutil.copy2("run_button.png", "test_folder/copy2.png")


# 폴더 복사
#shutil.copytree("test_folder", "test_folder2")  # 원본 폴더 경로, 대상 폴더 경로

# 폴더 이동
# shutil.move("test_folder", "test_folder2")
