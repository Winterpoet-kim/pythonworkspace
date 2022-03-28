"""
1. 리스트에 3개 이상의 단어를 추가
예) apple, banana, orange

2. 위 리스트에서 랜덤으로 1개의 단어를 선택

3. 단어의 길이에 맞게 밑줄 출력
예) apple 의 경우, _ _ _ _ _

4. 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct' 출력, 아니면 'Wrong' 출력

5. 매번 입력을 받을 때마다 현재까지 맞히 글자들 표시 (맞히지 못한 글자는 밑줄 출력)

6. 정답을 맞히면 Success 출력 후 프로그램 종료 (단, 횟수 제한은 없음.)

"""
from random import sample

lst = ['apple', 'banana', 'orange', 'coffee']
word = sample(lst, 1)
check_cnt = 0

char_lst = []
char_lst_copy = []

for w in word.pop():
    char_lst.append(w)
    char_lst_copy.append('_')

while True:
    result = False

    for c in char_lst_copy:
        print(c, end=" ")
    print()

    if check_cnt == len(char_lst):
        break

    input_w = input('Enter one word : ')

    for idx, c in enumerate(char_lst):
        if c == input_w:
            char_lst_copy[idx] = c
            check_cnt += 1
            result = True
    
    if result:
        print("Correct\n")
    else:
        print("Wrong\n")    

print("Succeed")


    
