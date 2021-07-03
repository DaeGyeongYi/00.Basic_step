def get_interest(dep,per):
    return dep*per/100

dep = int(input("예금액 입력: "))
per = float(input("이자율 입력(%%): "))

print("이자액: {}원".format(int(get_interest(dep,per)),","))