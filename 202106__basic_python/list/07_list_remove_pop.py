# 07_list_remove_pop.py
n = [1,2,3,3,4,5,4,3]
n.remove(4) #첫번 째 4 를 제거하고 원본반영됨
print(n) #[1, 2, 3, 3, 5, 4, 3]

# n리스트에서 원소값이 3인 원소를 모두 제거 하시오
# 3의 개수를 확인해야함
count = n.count(3) # 3개 들어 있음
for i in range(count) :
    n.remove(3)
    print("3 삭제 ", n)

print(n)

n1 = [1,1,2,1]
n1.remove(1)
n1.remove(1)
n1.remove(1)
# n1.remove(1) #ValueError: list.remove(x): x not in list - 요소 값이 없는데 remove 함수 사용하면 에러 발생
# 제거하기 전에 반드시 요소가 있는 지 확인하는게 좋다

# pop() : 리스트 마지막 요소 반환 하고 삭제
x = ['a','b','c','d']
y = x.pop() #'d'
print(y) # 반환된 마지막 요소 d
print(x) # d 삭제된 나머지 요소만 확인 ['a', 'b', 'c']

# x에 남아 있는 요소 3개를 pop
# 계속 pop 실행해서 더 이상 요소가 없으면 빈리스트로 남게됨
x.pop() #['a','b']
x.pop() #['a']
x.pop() #[]
print(x) #[]

#x가 빈리스트인 경우  pop()을하면 에러 발생
# x.pop() #IndexError: pop from empty list

#pop(인덱스) :  인덱스 위치에 있는 요소 반환 삭제
heroes = ['슈퍼맨','스파이더맨','헐크','아이언맨','베트맨']
tmp = heroes.pop(2) # 세번째 : 헐크 삭제
print('삭제된 값 :', tmp)
print('삭제 후 리스트', heroes)