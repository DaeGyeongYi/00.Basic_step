# 06_classmethod.py

# 클래스 메서드 : @staticmethod 키워드 사용
# 클래스명. 메서드 접근

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