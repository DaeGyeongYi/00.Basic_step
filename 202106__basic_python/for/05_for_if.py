# 아래 리스트에 저장되어 있는 점수에 대하여 합격/불합격을 판별하는 프로그램을 작성
# 합격은 60점 이상으로 설정

# 출력양식
# 1번 90점 합격
# 2번 57점 불합격

scores = [90,57,88,45,78]

# for score in scores :
#
#     if score >= 60 :
#         print("%d점 합격" % score)
#     else :
#         print("%d점 불합격" % score)

# 번호를 부착 해서 출력
number = 0
for score in scores :
    number = number + 1
    if score >= 60 :
        result = "합격"
    else :
        result = "불합격"

    print("%d번 %d점 %s" %(number,score,result))
