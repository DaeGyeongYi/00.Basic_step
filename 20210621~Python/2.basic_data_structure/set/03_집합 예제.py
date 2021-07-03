partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}


#파티에 참여한 모든사람
print(partyA|partyB)
#2개의 파이테 참석한 모든사람
print(partyA&partyB)
#파티 A만 참여한 사람
print(partyA-partyB)
#파티 B만 참여한사람
print(partyB-partyA)