# 사칙 연산 함수 작성
def add(a,b) :
    return a+b

def sub(a,b) :
    return a-b

def mul(a,b) :
    return a* b

def div(a,b) :
    return a/b

## 함수 호출 테스트
x=9
y=3

print("%d + %d = %d" % (x,y, add(x,y)))
print("%d - %d = %d" % (x,y, sub(x,y)))
print("%d * %d = %d" % (x,y, mul(x,y)))
print("%d / %d = %d" % (x,y, div(x,y)))