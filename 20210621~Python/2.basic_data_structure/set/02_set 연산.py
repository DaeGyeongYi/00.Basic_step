#02_set 연산
A={1,2,3}
B={3,4,5,6}
# a|b #합집합
print(A|B)
#a.union(b)
print(A.union(B))

print("=========================")
print(A&B) #교집합
#a.intersection(b)
print(A.intersection(B))

print("=========================")
print(A-B)
#a.difference(b)
print(A.difference(B))