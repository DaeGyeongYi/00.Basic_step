# 04_list_copy.py

# 리스트 변수 복사

a = [1,2,3]
#리스트 [1,2,3]을 메모리 어딘가 저장하고 저장되어 있는 주소를 a가 갖고 있다

# a 리스트의 값을 b 변수에 복사하시오.(저장하시오)
# 얕은 복사 : 원본을 변경하면 복사본 내용도 변경
b =  a
# a변수의 값을 b 변수에 저장하는 코드
# a가 갖고 있는 저장 주소를 b에게 저장

print(a)
print(b)

b[0] = 100

print(a)
print(b)
#b[0] 원소값을 변경 했는데   a[0] 원소값도 변경

# 깊은 복사 (deep copy)
# list() 함수 또는 deepcopy() 함수를 사용해서
# 리스트의 복사본을 새로 생성하여 반환
# 복사본 리스트 원소의 값을 변경하여도
# 원본 리스트 원소의 값은 변경되지 않음

scores = [1,2,3,4,5]
values = list(scores)
print(scores)
print(values)

values[0] = 100

#scores는 변경되지 않고  values만 변경 됨
print("scores : ", scores)
print("values : ", values) #values :  [100, 2, 3, 4, 5]

# deepcopy() 함수 : 깊은 복사
# copy 모듈을 import  해야함

import copy

a = ['a','b','c']
b = copy.deepcopy(a)

print("b 리스트 수정 전")
print(a)
print(b)

b[0] = 1

print("b 리스트 수정 후")
print(a)
print(b)