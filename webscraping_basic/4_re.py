# 정규식
import re

# abcd, book, desk
# ca?e
# care, cafe, case, cave...

p = re.compile("ca.e")  # p : 패턴
# . (ca.e): 하나의 문자를 의미 > care, cafe, case ...
# ^ (^de): 문자열의 시작 > desk, destination ...
# $ (se$): 문자열의 끝 > case, base ...

def print_match(m):
    #print(m.group())  # 매치되지 않으면 에러가 발생
    if m :
        print("m.group():", m.group())  # 일치하는 문자열을 반환
        print("m.string:",m.string)  # 입력받은 문자열
        print("m.start():",m.start())  # 일치하는 문자열의 시작 index
        print("m.end():", m.end())  # 일치하는 문자열의 끝 index
        print("m.span():", m.span())  # 일치하는 문자열의 시작, 끝 index
    else :
        print("매칭되지 않았습니다.")

m = p.match("careless")  # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

m = p.search("good care")  # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

lst = p.findall("good care cafe")  # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

