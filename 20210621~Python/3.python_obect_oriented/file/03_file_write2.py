#03_file_write2.py

# 여러행에 걸쳐 파일에 내보내기(쓰기)

f=open("file4.txt","w",  encoding='utf_8')

for i in range(1,11) :
    data = "%d행\n" % i
    f.write(data)

f.close()