# 03_class3_파라미터가 있는 생성자.py

# 생성자 함수 추가 2
# __ init__(self, 초기값 파라미터1, 초기값 파라미터2,....)

#  클래스 정의
#  name, age 2개의 속성을 정의- 생성자 파라미터로 기본값 저장
class person :
    #생성자 함수
    def __init__(self,name,age=10):
        self.name = name
        self.age = age
        print(self,' is generated')


# width, height 2개의 속성을 정의 - 생성자 파라미터로 기본값을 저장 기본값을 저장
class Rectangle :
    # 생성자 함수
    def __init__(self,width, height):
        self.width = width
        self.height = height

# person 객체 생성
# p0 = person()- 파이썬이 만들어주는 기본 생성자 함수는 개발자가 직접 생성자 함수 만들면 사용 불가
p1 = person('Bob',30)
p2 = person('Kate',20)
p3 = person('Aaron')

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)

# Rectangle  객체 생성
# r0 = Rectangle() - 파이썬이 만들어주는 기본 생성자 함수는 개발자가 직접 생성자 함수 만들면 사용 불가
r1=Rectangle(3,4)
r2 =Rectangle(10,2)

print(r1.width, r1.height)
print(r2.width, r2.height)
