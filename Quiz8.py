# Quiz 8

class House:
    count = 0
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_typ = deal_type
        self.price = price
        self.completion_year = completion_year
        House.count +=  1
    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_typ, self.price, self.completion_year))


sale1 =  House("강남", "아파트", "매매", "10억", "2010년")
sale2 =  House("마포", "오피스텔", "전세", "5억", "2007년")
sale3 =  House("송파", "빌라", "월세", "500/50", "2000년")

for_sales = []
for_sales.append(sale1)
for_sales.append(sale2)
for_sales.append(sale3)

print("총 {0}대의 매물이 있습니다.".format(House.count))

for sale in for_sales:
    sale.show_detail()



