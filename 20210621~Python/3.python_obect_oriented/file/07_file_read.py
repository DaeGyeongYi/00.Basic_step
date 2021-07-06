# 07_file_read.py
#read()함수 : 내용전체를 읽어서 1개의 문자열로 반환

f=open("test.txt",'r')
data=f.read()
print(data)

print(type(data))  #<class 'str'>
print(len(data)) #data의 글자수를 반환

# 1개 문자씩 출력
for ch in data :
    print(ch)