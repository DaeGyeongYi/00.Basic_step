# 여러값을 반환
def order() :
    pr = int(input("상품가격 입력 : "))
    qt = int(input("주문수량 입력 : "))
    amt = qt * pr
    return pr,qt, amt #튜플 형태로 반환

# 함수 호출
price, qty, amount = order()

print('-----------------------')
print("상품가격 : %d원" %price)
print("주문수량 : %d개" %qty)
print("주문액 :  %d원" %amount)