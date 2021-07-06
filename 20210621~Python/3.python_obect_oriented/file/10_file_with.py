# 10_file_with.py

with open("test3.txt",'w') as f :
    f.write("hello")

file ="test4.txt"
data='''Python programming
R programming
web programming'''

with open(file,'w') as f :
    f.write(data)