# 10_random.py
# 파이썬에서 난수(random number)를 사용하기 위해서는 기본적으로 제공되는 random 모듈 사용
#
# randint(최소, 최대)
# 최소부터 최대 사이의 임의의 정수 반환

from random import randint #random 모듈의 randint  함수 사용 준비
# n = randint(1, 100) # 1~100 사이이 정수로 난수를 발생
n = randint(1, 5) # 1~ 5
print(n)
