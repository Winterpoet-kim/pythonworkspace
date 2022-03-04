class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__() 다중 상속을 할경우는, 첫번째 상송 클래스만 적용되므로 명시적으로 사용할것
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍쉽 생성
dropship = FlyableUnit()