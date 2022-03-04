from tokenize import Double
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)


# 평점 구하기
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
sum_rate = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    sum_rate += float(rate)

print("평균 평점 : " , sum_rate/len(cartoons))
