# 02_file_write1.py

# 파일에 쓰기 : 파일을 쓰기모드(w)로 열고
# 파일 객체 변수의 wrtie()메서드로 출력값을 파일에 기록

# data = "hi"
data ='안녕하세요'
# f=open("file2.txt",'w')
f=open("file3.txt",'w',encoding='utf-8')
f.write(data) # 파일에 data 쓰기
f.close()