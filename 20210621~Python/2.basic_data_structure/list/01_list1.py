# 01_list1.py

#리스트 만들기
#변수명 = [값1,값2,....,값n]
#변수명 = [] - 빈리스트 생성

# 단일 자료형 list
ints = [1,2,3,4,5]
floats = [1.1,2.2,3.3,4.4,5.5]
names = ['홍길동','1','성춘향']

#복합 자료형  list
mix = [1, 5.0,'김철수']

# 리스트 안에 리스트를 포함할 수 있음
numbers = [100,200,300,[10,20,30]]

#리스트 반환
#리스트 명으로 접근
print(ints) #[1, 2, 3, 4, 5] 리스트 형태로 반환
print(floats)
print(names)
print(numbers)

# 각 원소 접근 - 원소 각각을 반환
for name in names :
    print(name)
    print(type(name))

# 각 원소를 인덱스를 통해 접근 - 원소값을 확인
for i in range(0,len(names)) :
    print(names[i])
    # print(i)

#  인덱스를 통해 원소에 접근
print(numbers[3])

# 리스트 각각의 값을 변수에 저장
nums = [1,2,3]
# 리스트 nums의 원소값 각각을  a,b,c 변수에 저장하시오
# a=nums[0]
# b=nums[1]
# c=nums[2]
#
# # a=b=c =0
# a,b,c = 1,2,3
a,b,c = nums #리스트 각각의 값을 차례대로 앞의 변수에 저장
print(nums)
print(a,b,c)

## 리스트 특징
nums1 = [10,20,30]
# a1,b1 = nums1 #ValueError: too many values to unpack (expected 2)
#왼쪽 변수의 개수가 오른쪽 리스트 원소의 개수보다 작으면 안된다
# a1,b1 = 10,20,30

# a1,b1,c1,d1 = nums1 #ValueError: not enough values to unpack (expected 4, got 3)
# 왼쪽 변수의 개수가 오른쪽 리스트 원소의 개수보다 많아도 안됨
# a1,b1,c1,d1 = 10,20,30
# print(a1,b1,c1,d1)

#