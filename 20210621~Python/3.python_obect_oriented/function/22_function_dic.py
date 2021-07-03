# 22_function_dic

students = [
    {"name":"홍길동","korean":87, "math":98,"english":88, "science":95},
    {"name":"이몽룡","korean":92, "math":98,"english":96, "science":98},
    { "name":"성춘향","korean":76, "math":96,"english":94, "science":90},
    { "name":"변학도","korean":98, "math":92,"english":96, "science":92},
    {"name":"박지성","korean":95, "math":98,"english":98, "science":98},
    {"name":"류현진","korean":94, "math":88,"english":92, "science":92}
]

# 딕셔너리를 전달받아서
# 딕셔너리의 일부만 추출 후 딕셔너리 구성 - 반환하는 함수

def get_student_subinfo(std_list) :
    # print(std_list)
    name = std_list["name"]
    korean = std_list["korean"]

    return {"name":name, "korean":korean}


std_sublist = []
# 리스트에서 딕셔너리를 함수에 전달하고
#반환된 name과 korean만 포함된 딕셔너리 받아서 std_sublist 변수에 추가
for s in students :
    std_info = get_student_subinfo(s)
    # print(std_info)
    std_sublist.append(std_info) #학생들 부분정보 dict를 리스트에 추가

print(std_sublist)

# [{'name': '홍길동', 'korean': 87}, {'name': '이몽룡', 'korean': 92}, {'name': '성춘향', 'korean': 76},
#  {'name': '변학도', 'korean': 98}, {'name': '박지성', 'korean': 95}, {'name': '류현진', 'korean': 94}]
