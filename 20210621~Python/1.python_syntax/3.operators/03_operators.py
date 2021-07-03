# 03_operators.py

# 현금이 5,000원이 있고, 사탕 가격이 120원인 경우
# 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?

myMoney = 5000
candyPrice = 120

#최대한 살 수 있는 사탕수
candies = myMoney // candyPrice

# 최대한 사탕을 구입하고 남은 돈
change = myMoney % candyPrice

print("사탕 %d 개를 사고 남은 돈 : %d 원" % (candies,change))
