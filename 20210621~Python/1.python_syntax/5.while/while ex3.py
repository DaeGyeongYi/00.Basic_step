# 사용자에게 숫자(정수)를 입력받아 홀수이면 아래 예시와 같이 출력하고＇짝수이면 출력 없이 다음 입력을 받는 프로그램을 작성하시오.
# 종료는 입력에 x 문자가 들어오면 종료하되  break 문을 활용하고,
# 짝수일 경우 출력의 건너뜀은  continue 문을  활용해 보시오

while True :
    s = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')

    if s == 'x' :
        print('종료합니다.')
        break

    if int(s) %2 == 0 :
        continue

    print(s + '는 홀수입니다.')
