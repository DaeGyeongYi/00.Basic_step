# 정수 3개를 입력 받아서 제일 큰 수 출력
 # 1.  정수 3개 입력받아 변수에 저장
num1 = int(input('정수 1 입력 : '))
num2 = int(input('정수 2 입력 : '))
num3 = int(input('정수 3 입력 : '))


# 2. 저장된 3개의 변수중 제일 큰수 판별
 # num1 이 가장 큰 경우  :  num1 > num2  and num1 > num3
if (num1 > num2)  and (num1 > num3) :
     print('제일 큰수 : ', num1) # 3. 판별된 제일 큰 수 출력
 # num1 이 제일 큰수 가 아니면  : num2 > num3 => num2 가 가장 큰수
elif num2 > num3 :
     print('제일 큰수 : ', num2) # 3. 판별된 제일 큰 수 출력
 # num2 도 제일 큰수가 아니면  : num3이 가장 큰 수
else :
     print('제일 큰수 : ', num3) # 3. 판별된 제일 큰 수 출력