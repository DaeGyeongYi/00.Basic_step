# 02_class2_ 생성자구현.py

#  클래스 정의
#  name, age 2개의 속성을 정의- 기본값을 저장
class person :
    #생성자 함수
    def __init__(self):
        self.name = 'Kate'
        self.age = 10
        print(self,' is generated')


# width, height 2개의 속성을 정의 - 기본값을 저장
class Rectangle :
    # 생성자 함수
    def __init__(self):
        self.width = 1
        self.height = 1

# person  클래스객체 생성
member1 = person()
member2 = person()

print("=== attribute 값 변경 전 ====")
print(member1.name, member1.age)
print(member2.name, member2.age)

member1.name='Kim'
member2.age=25

print("=== attribute 값 변경 후 ====")
print(member1.name, member1.age)
print(member2.name, member2.age)

#Rectangle 클래스 객체 생성
rect1 = Rectangle()
rect2 = Rectangle()

print("=== attribute 값 변경 전 ====")
print(rect1.width, rect1.height)
print(rect2.width, rect2.height)

rect1.width = 10
rect2.height=50

print("=== attribute 값 변경 후 ====")
print(rect1.width, rect1.height)
print(rect2.width, rect2.height)