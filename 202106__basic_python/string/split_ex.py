# split_ex.py

# 입력 코드
birthday = input("생일 입력 (연/월/일) : ")

birth_list = birthday.split('/')

# print(birth_list) #['1997', '10', '15']

print("당신은 %s년에 태어났고 " % birth_list[0] + '\n' +
      "생일은 %s월 %s일 이군요. " % (birth_list[1],birth_list[2]))