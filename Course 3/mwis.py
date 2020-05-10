file = open("mwis.txt", "r")
lines = file.readlines()
num_nodes = len(lines)
val = [0]
val.extend([int(line) for line in lines])

print(val)

A = [0] * (num_nodes+1)

for i in range(1, num_nodes+1):
    if i > 1:
        A[i] = max(A[i-1], A[i-2]+val[i])
    elif i == 1:
        A[i] = val[i]

print(A)

mwis = []

j = len(A)-1

while j > 0:
    if A[j-1] > A[j-2] + val[j] or A[j-1] == A[j-2] + val[j]:
        j = j-1
    else:
        mwis.append(j)
        j = j-2


print(mwis)

bits = ""
for i in [1, 2, 3, 4, 17, 117, 517, 997]:
    if i in mwis:
       bits =  bits + "1"
    else:
        bits = bits + "0"

print(bits)