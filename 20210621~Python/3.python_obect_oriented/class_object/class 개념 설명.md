## 객체지향 ?

객체 지향 프로그래밍에서는 모든 데이터를 객체(object)로 취급 => 객체가 바로 프로그래밍의 중심 
객체(object)란 간단히 이야기하자면 실생활에서 우리가 인식할 수 있는 사물(사람, 자동차, 핸드폰 등)
이러한 객체의 상태(state)와 행동(behavior)을 구체화하는 형태의 프로그래밍 =>객체 지향 프로그래밍
이때 객체를 만들어 내기 위한 설계도와 같은 개념을 클래스(class)라고 함



## Class 
실세계의 것(사물)을 모델링하여 속성(attribute)와 동작(method)를 갖는 데이터 타입
 python에서의 string, int, list, dict.. 모두가 다 클래스로 존재
 예를 들어 학생이라는 클래스를 만든다면, 학생을 나타내는 속성과 학생이 행하는 행동(동작)을 함께 정의 할 수 있음
 따라서, 다루고자 하는 데이터(변수) 와 데이터를 다루는 연산(함수)를 하나로 캡슐화(encapsulation)하여 클래스로 표현
 모델링에서 중요시 하는 속성에 따라 클래스의 속성과 행동이 각각 달라짐



## Object 
클래스로 생성되어 구체화된 객체(인스턴스)
파이썬의 모든 것(int, str, list..etc)은 객체(인스턴스)
실제로 class가 인스턴스화 되어 메모리에 상주하는 상태를 의미
class가 빵 틀이라면, object는 실제로 빵틀로 찍어낸 빵이라고 비유 가능



## 생성자 함수

`__init__(self):`

생성자, 클래스 인스턴스가 생성될 때 호출됨
rect1=Rectangle() #이 코드가 실행 시 호출
 self인자는 항상 첫번째에 오며 자기 자신을 가리킴
 이름이 꼭 self일 필요는 없지만, 관례적으로 self로 사용 
 생성자에서는 해당 클래스가 다루는 데이터를 정의
 이 데이터를 멤버 변수(member variable) 또는 속성(attribute)라고 함



## self

파이썬의 method는 항상 첫번째 인자로 self를 전달
self는 현재 해당 메쏘드가 호출되는 객체 자신을 가리킴
C++/C#, Java의 this에 해당
역시 이름이 self일 필요는 없으나, 위치는 항상 맨 처음의 parameter이며 관례적으로 self로 사용



## class method

instance method - 객체로 호출(일반 method)
메쏘드는 객체 레벨로 호출 되기 때문에, 해당 메쏘드를 호출한 객체에만 영향을 미침
class method(static method) –> @staticmethod 사용
클래스 메쏘드의 경우, 클래스 레벨로 호출되기 때문에, 클래스 멤버 변수만 변경 가능

<u>즉, 인스턴스를 생성하지 않고도 내부의 함수를 사용할 수 있게 해줌</u>

```python
class Math :
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def multiply(a,b):
        return(a*b)

# 클래스 메서드 사용
print("클래스 메서드로 접근 : ",  Math.add(10,20))
print("클래스 메서드로 접근 : ",  Math.multiply(10,20))

#
m_obj = Math()
print("객체(인스탄스) 메서드로 접근 : ",m_obj.add(3,4))
print("객체(인스탄스) 메서드로 접근 : ",m_obj.multiply(3,4))
```

