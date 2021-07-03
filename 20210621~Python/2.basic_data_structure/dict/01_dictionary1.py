#key:value로 이루어진 자료구조
#쉼표(,)로 item 구분함
#순서가 없다. -> 인덱스로 접근할 수 없다.
#key:value의 한쌍을 item이라고 함.

#딕셔너리 생성

d= {1:'a'}
print(d)
print(type(d))

#item 추가, (key-2 : value -'b')
d[2] = 'b' #2가 인덱스가 아니라 key에요!
print(d)

#item 추가
#key는 문자도 가능
d['test'] = 'valueTest'
print(d)

naver = {"name" : "naver",
         "url":"www.naver.com",
         "userid" : "nv",
         "password" :"1234"}
print(naver)
print("============================")

#dict 필수함수

print(naver.keys())
print(naver.values())
print(naver.items())
#전부 다 리스트 형태로 반환 -> 형변환

print(type(naver.keys()))#key를 리스트 형태로 반환
print(type(naver.values()))
print(type(naver.items()))

#tuple로 변환
to_tuple = tuple(naver.keys())
print(to_tuple)
print(type(to_tuple))