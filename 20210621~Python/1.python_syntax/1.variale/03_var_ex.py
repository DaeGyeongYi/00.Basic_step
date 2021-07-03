name = '홍길동'
no = '2016001'
year = 4
grade = 'A'
average = 93.5
level = 10

#포맷코드 사용
print("성명 : %s" % name)
print("학번 : %s" % no)
print("학년 : %d" % year)
print("학점 : %c" % grade)
print("평균 : %.2f" % average)
print("등급 : %d %%" % level) #등급 : 10% - %문자를 출력 %%