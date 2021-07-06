# 08_file_search.py
# 파일 내에서 검색 예제
 # read() 함수 이용해서 파일 내용을 문자열로 저장

f=open("test2.txt","r",encoding='utf-8')
data=f.read() # test2.txt  파일내용을 문자열로 data 변수에 저장

#검색값 입력
value = input("검색 값 입력 : ")

#문자열에 검색 값이 있는지 확인
if value in data :
    print("있음")
else :
    print("없음")

f.close()