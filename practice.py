# print(5)
# print(-10)
# print(3.14)
# print(1000)
# # print('풍선')
# print(True)

# station1 = "사당"
# station2 = "신도림"
# station3 = "인천공항"

# print(station1, "행 열차가 들어오고 있습니다")
# print(station2, "행 열차가 들어오고 있습니다")
# print(station3, "행 열차가 들어오고 있습니다")


# from math import *

# print(floor(4.99)) #내림
# print(ceil(3.14)) #올림
# print(sqrt(16)) #제곱근

# from random import *

# print(random())
# print(int(random()*10))


# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)

#print(randrange(1, 46), randrange(1, 46), randrange(1, 46), randrange(1, 46), randrange(1, 46), randrange(1, 46))

# off_date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월", str(off_date), "일로 선정되었습니다.")



#문자열 포맷 방법1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요." % "A")

# print("나는 %s살입니다." %20)
# print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

#문자열 포맷 방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))

#문자열 포맷 방법3
#print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))

# #문자열 포맷 방법4
# age = 20
# color ="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출문자
# \n : 줄바꿈
#print("백문이 불여일견\n백견이 불여일타")

# \" : 문장 내에서 따옴표 인식
# 저는 "겨울시인" 입니다.
# print("저는 '겨울시인'입니다.")
# print('저는 "겨울시인"입니다.')
# print("저는 \"겨울시인\"입니다.")

# # \\ : 문장 내에서 \ 하나로 인식
# print("C:\\Users\\admin\\Desktop\\Code\\pythonworkspace")

# # \r : 커서를 맨 앞으로 이동
# print("11111Apple\rPine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")


# Quiz

# url = "http://daum.net"
# print(f"전체 주소 = {url}")
# #addr = url[7:] 방법1
# addr = url.replace("http://", "") #방법2
# # print(f"http:// 삭제 = {addr}")

# addr = addr[:addr.index(".")]
# # print(f".com 제외 = {addr}")

# length = len(addr)
# # print(f"글자수 = {length}")

# addr1 = addr[:3]
# #  print(f"처음 세글자 = {addr1}")

# # # 글자 내 'e' 갯수
# count = url.count("e")
# # print(f"e의 갯수 = {count}")

# pw = addr1 + str(length) + str(count) + "!"
# print(f"생성된 비밀번호 = %s" % pw)


# 리스트 [] 

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇번째 칸에 타고 있는가
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 탑승
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석 - 조세호 사이에 
# subway.insert(1, "정형돈")
# print(subway)

# # 한명씩 하차
# subway.pop()
# print(subway)
# subway.pop()
# subway.pop()
# print(subway)

# # 같은 이름의 사람이 몇 명이 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))


# 정렬
# num_list = [5,2,4,1,3]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list = [5,2,4,1,3]

# num_list.extend(mix_list)
# print(num_list)


# # 사전
# cabinet = {3:"유재석", 100:"조세호"}
# # [] 를 쓸때, 없는 key를 찾았으면 오류발생 -> 프로그램 종료
# print(cabinet[3])
# print(cabinet[100])

# # get(key) 함수를 쓰고, 없는 key를 찾으면 none을 return 
# print(cabinet.get(3))
# print(cabinet.get(100))
# print(cabinet.get(5))
# print("Hi")
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet)
# print(5 in cabinet)

# # 새 손님
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["C-20"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())
# # value 들만 출력
# print(cabinet.values())
# # key, value 쌍으로 출력
# print(cabinet.items())

# # 클리어
# cabinet.clear()
# print(cabinet)


# tuple 튜플 (내용 추가나 변경 못하지만 속도는 빠름)
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)


# set 세트 (집합) = 중복이 안되고, 순서가 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java와 python을 모두 할수있는 개발자)
# print(java&python)
# print(java.intersection(python))

# # 합집합
# print(java|python)
# print(java.union(python))

# # 차집합
# print(java - python)
# print(java.difference(python))

# python.add("김태호")
# print(python)
# python.remove("김태호")
# print(python)




# 자료구조의 변경

# menu = {"커피", "주스", "우유"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


# from random import *

#id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# id_list = range(1,21) # 1부터 20까지 숫자 생성
# id_list = list(id_list)

# shuffle(id_list)
# print(id_list)

# win_chicken = id_list.pop(0)
# shuffle(id_list)

# win_coffee_list = []
# win_coffee_list.append(id_list.pop(0))

# shuffle(id_list)
# win_coffee_list.append(id_list.pop(0))

# shuffle(id_list)
# win_coffee_list.append(id_list.pop(0))

# print("--- 당첨자 ---")
# print("치킨 당첨자 = " + str(win_chicken))
# print("커피 당첨자 = " + str(win_coffee_list))

# print("--- 축하합니다. ---")



# 분기 if

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")


# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무더워요")
# elif 10 <= temp and temp < 30 :
#     print("괜찮은 날씨")
# elif 0 <= temp < 10 :
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요. 나가지 마세요")



# 반복문 for

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 {0}" .format(waiting_no))

# for waiting_no in range(1, 11, 2):
#     print("대기번호 {0}" .format(waiting_no))

# starbucks = ["A", "B", "C"]
# for customer in starbucks :
#     print("{0} 커피가 준비됐습니다." .format(customer))



# 반복문 while

# customer = "A"
# index = 5
# while index >= 1 :
#     print("{0} Ready Coffee {1} remains." .format(customer, index))
#     index -=  1
#     if index == 0 :
#         print("Coffee is end.")

# customer = "B"
# index = 1
# while True : # 무한루프
#     print("{0} Coffee is Ready! index = {1}" .format(customer, index))
#     index += 1

# customer = "C"
# person = "Unknown"
# while person != customer :
#     print("{0} Coffee is Ready! " .format(customer))
#     person = input("what's your name : ")a



# continue, break 

# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11) :
#     if student in absent :
#         continue
#     elif student in no_book :
#         print("End Class!!")
#         break
#     print("Read books {0}" .format(student))


# 한줄 for

# 출석번호가 1,2,3,4.. 앞에 100을 붙이기로 함. - > 101, 102, 103, 104 ...

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변황

# students = ["AAAA", "BB", "CCCCC", "DDD"]
# name_length = [len(i) for i in students]
# print(students)
# print(name_length)

# students = [i.lower() for i in students]
# print(students)

# from random import *

# count = 0
# for customer in range(1, 51) :
#     time = randrange(5, 51)
#     if 5<= time <= 15 :
#         print("[o] {0}번째 손님 (소요시간 :  {1}분" .format(customer, time))
#         count += 1
    
#     else :
#         print("[ ] {0}번째 손님 (소요시간 :  {1}분" .format(customer, time))
    
# print("total customer : {0}명" .format(count))


# 함수

# def open_account() :
#     print("New Account Open")
# open_account()

# 전달값과 반환값

# def deposit(balance, money) :
#     print("입금완료. 잔액은 {0}입니다." .format(balance+money))
#     return balance+money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금 완료 잔액은 {0}원입니다." .format(balance-money))
#         return balance-money
#     else :
#         print("잔액이 부족합니다.")
#         return balance

# def withdaw_night(balance, money) :
#     commission = 100
#     return commission, balance-money-commission

        
# balance = 0
# balance = deposit(balance, 20000)
# commission, balance = withdaw_night(balance, 5000)
# print("수수료 {0}원이며, 잔액은 {1}원입니다." .format(commission, balance))


# 함수 기본값 설정

# def profile(name, age, main_lang):
#     print("name = {0}\t, age = {1}\t language = {2}") .format(name, age, main_lang)


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age=17, main_lang="파이썬"):
#     print("name = {0}\t, age = {1}\t language = {2}" .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 키워드값
# def profile(name, age, main_lang):
#     print("name = {0}\t, age = {1}\t language = {2}" .format(name, age, main_lang))

# profile(name="유재석", age=20, main_lang="파이썬")
# profile(main_lang="자바", age=25, name="김태호")


# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name = {0}\t, age = {1}\t" .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "python", "java", "c++", "c#", "c")
# profile("김태호", 25, "kotlin", "swift", "", "", "")

# def profile(name, age, *language):
#     print("name = {0}\t, age = {1}\t" .format(name, age), end=" ")
#     for lang in language :
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "java", "c++", "c#", "c", "jacascript")
# profile("김태호", 25, "kotlin", "swift")

# 지역변수와 전역변수
# 일반적으로 전역변수를 많이쓰면 코드 관리가 어려움
# 함수의 전달값(파라미터)를 통해 던져서 계산하고 return값을 받아서 사용을 권장

# gun = 10
# def checkpoint(soldiers) : #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 = {0}".format(gun))


# def checkpoint_return(gun, soldiers) : #경계근무
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 = {0}".format(gun))
#     return gun

# print("전체 총수 = {0}".format(gun))
# #checkpoint(2)  # 2명이 경계근무 나감.
# gun = checkpoint_return(gun, 2)  # 2명이 경계근무 나감.
# print("남은 총수 = {0}".format(gun))


# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else :
#         return height * height * 21        

# height = 175
# gender = "남자"
# weight = round((std_weight(height/100, gender)),2)
# # 소수점 2째 자리에서 반올림 -> ex) round(num, 2)


# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


# 표준 입출력

# print("python", "java", sep=",")
# print("python", "java", sep=" vs ")
# print("python", "java", sep=",", end="?")
# # end의 의미는 기존의 끝부분인 줄넘기기를 ?로 대체하고 다음 문장을 이어붙여서 출력
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) #표준 출력으로 문장이 찍힘
# print("Python", "Java", file=sys.stderr) #표준 에러로 문장이 찍힘

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
    
#     #왼쪽정렬, 오른쪽정렬
#     print(subject.ljust(8), str(score).rjust(4), sep=":") 


# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) #zfill 3개 공간확보하고 나머지를 0으로 채우기


# answer = input("아무값이나 입력하세요 : ")
# print(type(answer))  #즉 항상 문자열 타입으로 저장됨.
# print("입력하신 값은 " + answer + "입니다.")

# 다양한 출력 포맷

# # 1. 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 2. 양수일때는 +로 표시, 음수일때는 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >-10}".format(-500))
# # 3. 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))
# # 4. 3자리마다 ,를 찍음
# print("{0:,}".format(10000000))
# # 5. 3자리마다 ,를 찍고, +- 부호도 찍기
# print("{0:+,}".format(10000000))
# print("{0:-,}".format(-10000000))
# # 6. 3자리마다 ,를 찍고, 부호도 붙이고, 자릿수도 확보, 빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(100000000))
# # 7. 소숫점 출력
# print("{0:f}".format(5/3))
# # 8. 소숫점을 특정 자리까지 출력 (소숫점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))


# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file) #자동 줄바뀜
# print("영어 : 50", file=score_file)
# score_file.close()

# # a의 의미는 append
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80\n")  # 자동 줄바뀜이 없으므로 \n을 붙여야함.
# score_file.write("코딩 : 100\n")
# score_file.close()

# 파일의 모든 내용 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) 
# score_file.close()

# 파일의 한줄 내용 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline(), end="") # 줄바꿈을 안하고 싶을때
# print(score_file.readline())
# score_file.close()

# 총 몇줄인지 모를때 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# list에 모든값을 넣어서 처리
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()



# 피클 pickle

# import pickle
# profile_file = open("profile.pickle", "wb") # b는 바이너리, endcoding은 따로 설정할 필요없음
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()


# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()



# with

# import pickle

# # with open("profile.pickle", "rb") as profile_file:
# #     print(pickle.load(profile_file))

# # with open("study.txt","w", encoding="utf8") as study_file:
# #     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt","r", encoding="utf8") as study_file:
#     print(study_file.read())


# for i in range(1, 3):
#     file_name = str(i)+"주차.txt"
#     print(file_name)
#     report_file = open(str(file_name), "w", encoding="utf8")
#     report_file.write("- {0} 주차 주간보고 - \n".format(i))
#     contents_1 = ["부서 : \n", "이름 : \n", "업무 요약 : \n"]
    
#     for content in contents_1:
#         report_file.write(content)
#     report_file.close()




# 클래스 class

# # 마린 : 공격 유닛, 군인, 총을 쏠수있음.
# name = "마린"
# hp = 40 
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# # 탱크 : 공격 유잇, 탱크, 포를 쏠수있음, 일반모드/시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군으 공격합니다. [공격력{2}]".format(name,location,damage))


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)


# 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage) : # 생성자 : 클래스 호출시 자동으로 호출되는 부분
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0}유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# marine1 = Unit("마린", 40, 5)  # marine과 tank는 Unit 클래스의 인스턴스라 함.
# marine2 = Unit("마린", 40, 5)
# tank1 = Unit("탱크", 150, 35)


# 멤버 변수  ex) self.namem, self.hp, self.damage 들이 멤버변수
# 클래스 내에서 정의된 변수

# 레이스 : 공중 유닛, 비행기, 클로킹 기능 (상대에게 보이지 않음)
# wraith = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}" .format(wraith.name, wraith.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True #클래스에 선언되지 않은 추가 변수를 선언, 할당함.
# # 객체에 변수를 만들어 추가로 쓸수있음. 파이썬만의 특징??

# if wraith2.clocking == True :
#     print("{0}는 현재 클로킹 상태입니다." .format(wraith.name))


# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp) : 
#         self.name=name
#         self.hp=hp
        

# # 공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage) : #self는 자기자신.
#         self.name=name
#         self.hp=hp
#         self.damage=damage

#     def attack(self, location): # 클래스 내 메소드 안에는 무조건 적어주어야함.
#         print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]".format(self.name, location, self.damage))
#         #self.name, self.damage의 경우 클래스 내에 있는 멤버변수를 사용한다는 말.
#         #location의 경우 전달받은 값을 쓴다는 의미.

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은  {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))
    

# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)



# 상속

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp) : 
#         self.name=name
#         self.hp=hp
        

# # 공격 유닛
# class AttackUnit(Unit):  # Unit=부모 클래스, AttackUnit=자식 클래스
#     def __init__(self, name, hp, damage) : 
#         Unit.__init__(self, name, hp)
#         self.damage=damage

#     def attack(self, location): 
#         print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]".format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은  {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)



# # 다중 상속 : 부모 클래스가 2개 이상


# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp ,speed) : 
#         self.name=name
#         self.hp=hp
#         self.speed=speed

#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
        

# # 공격 유닛
# class AttackUnit(Unit):  
#     def __init__(self, name, hp, speed, damage) : 
#         Unit.__init__(self, name, hp, speed)
#         self.damage=damage

#     def attack(self, location): 
#         print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]".format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은  {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.fylying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.fylying_speed))


# # 공중 공격 유닛 클래스
# class FylableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, fly_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로 세팅
#         Flyable.__init__(self, fly_speed)


# # 발키리 : 공격유닛, 한번에 14발 미사일 발사
# # valkyrie = FylableAttackUnit("발키리", 200, 6, 5)
# # valkyrie.fly(valkyrie.name, "3시")




# # 메소드 오버라이딩

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루져 : 공중 유닛, 체력 좋고, 공격력 좋음
# battlecruiser =  FylableAttackUnit("배틀크루져", 500, 25, 3)

# vulture.move("2시")
# battlecruiser.fly(battlecruiser.name,"11시")




# 예외처리

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요: ")))
#     nums.append(int(input("첫번째 숫자를 입력하세요: ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러 : 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print(err)
#     print("알수없는 에러가 발생하였습니다.")


# 에러 발생시키기.

# try:
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("첫번째 숫자를 입력하세요: "))
#     if num1 >=10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")


# 사용자 정의 예외처리

# class BigNumerError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("첫번째 숫자를 입력하세요: "))
#     if num1 >=10 or num2 >= 10:
#         raise BigNumerError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
# except BigNumerError as err:
#     print(err)
#     print("에러 발생. 한자리 숫자만 입력하세요")
# # finally : 정상적으로 실행되든, 에러가 발생하든 무조건 실행되는 구문
# # try 문 내에서 마지막에 쓸수있음.
# finally:
#     print("계산기를 사용해 주셔서 감사합니다.")



# 모듈

# import theater_module

# theater_module.price(3)  #3명이서 영화 보러갔을때 가격
# theater_module.price_morning(4)  #4명이서 영화 보러갔을때 가격
# theater_module.price_soldier(5)  #5명이서 영화 보러갔을때 가격

# import theater_module as mv

# mv.price(3)  #3명이서 영화 보러갔을때 가격
# mv.price_morning(4)  #4명이서 영화 보러갔을때 가격
# mv.price_soldier(5)  #5명이서 영화 보러갔을때 가격


# from theater_module import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning

# price(3)
# price_morning(4)

# from theater_module import price_soldier as price

# price(5)




# 팩키지 : 모듈들을 모아놓은 집합

# import travel.thailand
# #import 파일이름.(모듈 or 팩키지)
# #즉, 클래스나 함수는 직접 import 할수 없음.

# trip_th = travel.thailand.ThailandPackage() # 객체 생성
# trip_th.detail()

# from travel.vietnam import VietnamPackage

# trip_vi = VietnamPackage()
# trip_vi.detail()


# __all__

# from travel import *
# # travel 폴더 안의 __init__ 작성해서 공개 범위를 설정해야 모두 가져다 쓸수 있음.

# trip_vi = vietnam.VietnamPackage()
# trip_vi.detail()


# # 모듈을 직접 실행/호출해서 실행

# trip_th = thailand.ThailandPackage() # 객체 생성
# trip_th.detail()


# 패키지, 모듈 위치

# import inspect
# import random
# from travel import *

# print(inspect.getfile(random))
# print(inspect.getfile(thailand))



# pip install

# https://pypi.org/


# BeautifulSoup 예제

# from bs4 import 
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# 터미널 : pip list   : 현재 설치된 패키지를 볼수있음.
# 터미널 : pip show beautifulsoup4 : 설치된 패키지의 정보
# 터미널 : pip install --upgrade beautifulsoup4 : 설치된 패키지의 업그레이드
# 터미널 : pip uninstall beautifulsoup4 : 설치된 패키지의 삭제



# 내장 함수 : 따로 import 할 필요없이 사용할 수 있는 함수.
# ex) input()
# ex) dir() : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# import random
# print(dir(random))

# lit = [1,2,3]
# print(dir(lit))

# name = "Jim"
# print(dir(name))

# 내장 함수 정보
# list of python builtins 검색 -> https://docs.python.org/3/library/functions.html


# 외장 함수 : 직접 import 해서 사용하는 함수
# list of python modules 검색 -> https://docs.python.org/ko/3/py-modindex.html

# 외장 함수 예제1) glob : 경로 내의 폴더 / 파일 목록 조회(윈도우의 dir)
# import glob
# print(glob.glob("*.py"))

# 외장 함수 예제2) os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())


# 외장 함수 예제3) time : 시간관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 : ", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days=100)  # 100일 저장
# print("우리가 만난지 100일은 ", today+td) # 오늘부터 100일 후


# import byme

# byme.sign()