katok = ['다현','정연','쯔위','미나','사나','지효','모모']

def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1,kLen,1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])


print(katok)
delete_data(4)
print(katok)