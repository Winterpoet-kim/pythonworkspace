# lst = [1,2,3,4,5]
# lst.reverse()
# print(lst)

# lst2 = [1,2,3,4,5]
# print("리스트2 뒤집기 전 : ", lst2)

# lst3 = reversed(lst2)
# print("리스트2 뒤집은 후 : ", lst2)
# print("리스트3 :", list(lst3))


kor = ["사과", "바나나", "오렌지"]
eng =  ["apple", "banana", "orange"]

print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
#print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)