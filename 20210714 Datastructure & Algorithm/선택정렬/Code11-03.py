## 함수
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in  range(i+1, n):
            if ary[minIdx] > ary[k]:
                minIdx = k
        ary[i],ary[minIdx],= ary[minIdx], ary[i]
    return ary


## 전역
import random
before = [random.randint(10,99) for _ in range(20)]
after = []


##메인
print('정렬 전-->')
print(before)
print('정렬 후-->')
print(selectionSort(before))