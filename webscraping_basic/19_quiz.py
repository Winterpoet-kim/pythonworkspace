# 부동산 매물 (송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# [조회 조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ============ 매물1 =============
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# ============ 매물2 =============
#     ...

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

url = "https://realty.daum.net/home/apt/danjis/38487"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

items = soup.find_all("div", attrs={"class":"css-1dbjc4n"})
print(len(items))
# print(items)

for item in items:    
    try:
        date = item.find("div", attrs={"class":"css-1dbjc4n r-1wbh5a2 r-1w6e6rj"}).get_text()
        print(date)
    except AttributeError:
        #print("텍스트 속성이 없습니다.")
        continue
 

