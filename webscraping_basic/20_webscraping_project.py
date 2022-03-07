import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

url_1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.asiw&fbm=0&acr=1&acq=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
res = requests.get(url_1)
res.raise_for_status()

soup_1 = BeautifulSoup(res.text, "lxml")

with open("project.html", "w", encoding="utf8") as f:
    f.write(soup_1.prettify())

print("[오늘의 날씨]")
weather = soup_1.find("p", attrs={"class":"summary"}).get_text()
print(weather)
tempo = soup_1.find("div", attrs={"class":"temperature_text"}).get_text()
low = soup_1.find("span", attrs={"class":"lowest"}).get_text()
high = soup_1.find("span", attrs={"class":"highest"}).get_text()
print(tempo.strip(), "("+low+" "+high+")")

rain = soup_1.find_all("span", attrs={"class":"rainfall"})
print("오전 강수확률 {}  /  오후 강수확률 {}".format(rain[0].get_text(), rain[1].get_text()))

mise = soup_1.find_all("span", attrs={"class":"txt"})
print(f"미세먼지 : {mise[0].get_text()}")
print(f"초미세먼지 : {mise[1].get_text()}")
print(f"자외선 : {mise[2].get_text()}")
print(f"일몰시간 : {mise[3].get_text()}")


url_2 = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"

res2 = requests.get(url_2, headers=headers)
res2.raise_for_status()

soup_2 = BeautifulSoup(res2.text, "lxml")

with open("project_2.html", "w", encoding="utf8") as f2:
    f2.write(soup_2.prettify())

print("[IT 뉴스]")

headlines = soup_2.find("ul", attrs={"class":"type06_headline"}).find_all("dt")


for index, headline in enumerate(headlines):
    
    if index/2 == 3:
        break
    
    if (index+1)%2 == 0  :
        print(str(int((index+1)/2)) + "." + headline.get_text().strip())
        link = headline.a["href"]
        print(link)
        
    else :
        continue
    