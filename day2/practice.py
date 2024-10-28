class Fourcal:
    def __init__(self):
        self.name = "정선우"
        self.sex = "male"
        self.age = 25

    def introduce(self):
        print(f"저는 {self.name}이고, 나이는 {self.age}인 {self.sex}입니다.")

sunwoo = Fourcal()
sunwoo.introduce()

class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
 
james = Person()
james.greeting()    # 안녕하세요.


