#for_ex5
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

a = 0
for i in range(3) :
    # a+=1 #  이 문장의 수행 횟수는? 3회
    for j in range(4) :
        # a +=1 # 이 문장의 수행 횟수는? 12회
        print(a, end="\t")
        a += 1  # 최종  a 의 값은? 이 문자의 수행 횟수는? 12회
    print()

print(a)
