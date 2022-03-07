import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

def create_soup(url, headers):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrape_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.asiw&fbm=0&acr=1&acq=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url, headers)

    print("[오늘의 날씨]")
    weather = soup.find("p", attrs={"class":"summary"}).get_text()
    print(weather)
    tempo = soup.find("div", attrs={"class":"temperature_text"}).get_text()
    low = soup.find("span", attrs={"class":"lowest"}).get_text()
    high = soup.find("span", attrs={"class":"highest"}).get_text()
    print(tempo.strip(), "("+low+" "+high+")")

    rain = soup.find_all("span", attrs={"class":"rainfall"})
    print("오전 강수확률 {}  /  오후 강수확률 {}".format(rain[0].get_text(), rain[1].get_text()))

    mise = soup.find_all("span", attrs={"class":"txt"})
    print(f"미세먼지 : {mise[0].get_text()}")
    print(f"초미세먼지 : {mise[1].get_text()}") 
    print(f"자외선 : {mise[2].get_text()}")
    print(f"일몰시간 : {mise[3].get_text()}")
    print()


def scrap_it_news():
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url, headers)

    print("[IT 뉴스]")
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)

    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1
        
        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("   (링크 : {})".format(link))
        print()


def scrap_hackers():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url, headers)

    contents = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})  # 정규식 사용
    
    print("(영어 지문)")
    total_contents = len(contents)

    # 방법 1.
    # for i in range(int(total_contents/2), total_contents):
    #     print(contents[i].get_text().strip())
    # 방법 2.
    for content in contents[len(contents)//2:]:
        print(content.get_text().strip())
    
    print("(한글 지문)")
    # # 방법 1.
    # for i in range(0, int(total_contents/2)):
    #     print(contents[i].get_text().strip())
    # 방법 2.
    for content in contents[:len(contents)//2]:
        print(content.get_text().strip())
                   
    print()


if __name__ == "__main__":
    scrape_weather()  # 오늘의 날씨 정보 가져오기
    scrap_it_news()  # IT 뉴스 3개 가져오기
    scrap_hackers() # 
    

