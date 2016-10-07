#4.04

sc = [
['tooth paste', 'q-tips', 'milk'],
['milk', 'candy', 'apples'],
['planner', 'pencils', 'q-tips']
]

print(len(sc))

j=-1
rev = []

for i in range(0,3):
    arr = list()
    # switch 1st and last of s[j]
    temp = sc[j][0]
    sc[j][0] = sc[j][2]
    sc[j][2] = temp
    arr.append(sc[j])
    j = j-1
    rev.append(arr)
    
print(rev)


