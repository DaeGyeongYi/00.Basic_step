#01_set.py

# 집합 만들기 : {}  이용
s1 = {1,2,3,4,5}
print(s1) #{1, 2, 3, 4, 5}
print(type(s1)) #<class 'set'>

# set() 함수로 집합 만들기
#
s2 = set([10,20,30]) #리스트 -> set 형으로 형변환
print(s2) #{10, 20, 30}
print(type(s2)) #<class 'set'>

s3 = set((100,200,300)) #튜플 -> set 형으로 변환
print(s3) #{200, 100, 300}
print(type(s3))

print("=====================")

s4 = {1,2,3,3,4} # 중복값을 set에 저장 - 에러나지는 않는다
print(s4) # 저장할때 중복값은 1번만 저장 {1, 2, 3, 4}

# {}이용해서 리스트를 집합에 추가하면 에러 발생
# s5 = {1,2,[3,4]} TypeError: unhashable type: 'list'
# print(s5)

# 인덱스 사용 불가
# print(s4[0]) TypeError: 'set' object is not subscriptable

# s6 = {1,2,{2,3}} TypeError: unhashable type: 'set'

# 집합에 요소 추가, add() - 1개의 요소 추가
s={1,2,3}
s.add(4)
print(s)

# 집합에 요소 추가, update() - 여러개 추가 시
s.update([5,6])
# s.update(5,6)  #TypeError: 'int' object is not iterable
s.update((5,6))
# s.update(5)TypeError: 'int' object is not iterable
print(s) #{1, 2, 3, 4, 5, 6}

# 요소 제거
s.remove(3)
print(s) #{1, 2, 4, 5, 6}

# 전체 요소 삭제
s.clear()
print(s) #set() : 빈 집합의 의미

# 집합 삭제
del s #s 변수 삭제됨
print(s) #NameError: name 's' is not defined