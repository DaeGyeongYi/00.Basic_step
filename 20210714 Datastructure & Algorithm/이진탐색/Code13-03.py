## 함수
def binSearch(ary, fData) :
    pos = -1 #에러검출용
    start = 0
    end = len(ary)-1
    while (start <= end) : #처음부터 끝까지
        mid = (start + end) // 2 #중간값
        if fData == ary[mid] : #찾는 데이터와 중간값이 같다면?
            return  mid        # 그거리턴해
        elif findData > ary[mid] : # 찾는 데이터가 더 크다면
            start = mid + 1       # 왼쪽은 버리고 다시 (start를 mid다음 숫자로 지정함)
        else :                    #찾는 데이터가 더 작다면
            end = mid - 1         # 오른쪽은 버리고 다시 (end를 mid보다 하나 작은 숫자로 지정)
    return  pos #아무일도 없이 함수가 종료되면 에러

## 변수
# dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
# findData = 166 # 할머니키
import random
dataAry = [ random.randint(1000000, 9999999) for _ in range(500) ]
dataAry.insert(250, 5000000)
dataAry.sort()
findData = 5000000

## 메인
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)  # -1
if position == -1 :
    print('못 찾음...')
else :
    print(findData, '는', position, '위치에 있음')