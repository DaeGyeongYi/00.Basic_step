katok = ['다현','정연','쯔위','사나','지효','모모']

def insert_data(position, friend):
    katok.append(None) #배열의 길이를 하나 늘림
    kLen = len(katok)

    for i in range(kLen-1,position,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend


print(katok)
insert_data(3,'미나')
print(katok)
