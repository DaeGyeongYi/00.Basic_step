# 09_중첩for_구구단.py

# 구구단 출력 2단부터 9단까지 출력

# for dan in range(2,10) :
#     for n in range(1,10) :
#         print("%d * %d = %d" % (dan,n,dan*n))
#
#     print()

for n in range(1,10) :
    for dan in range(2,10) :
        print("%d * %d = %2s" % (dan,n,str(dan*n)), end="\t")

    print()