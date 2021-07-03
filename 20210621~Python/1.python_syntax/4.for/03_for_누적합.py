# 03_for_누적합.py

sumx = 0 # 누적변수는 사용하기 전에 반드시 선언(초기화, 준비)해야 함
# 1부터 10까지 출력하고 1-10까지 더한 결과도 출력하는 프로그램을 작성하시오
for x in range(1,11) :
    print(x)
    # sumx = sumx + x
    sumx += x
print('1부터 10까지 누적 합 : ' ,sumx)
# x 가 1일때 sumx 는 0인상태에서  sumx = sumx + x
# x 가 2일때 sumx 는 1인상태에서  sumx = sumx + x
# x 가 3일때 sumx 는 3인상태에서  sumx = sumx + x
# x 가 4일때 sumx 는 6인상태에서  sumx = sumx + x

sumx = 0
## 1부터 100까지 더하는 프로그램을 작성하세요
for x in range(1,101) :
    # print(x)
    # sumx = sumx + x
    sumx += x
print('1부터 100까지 누적 합 : ' ,sumx)