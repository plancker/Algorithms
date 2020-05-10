import heapq
from copy import deepcopy
file = open("huffman.txt", "r")
lines = file.readlines()
freq = []
for i in range(0, len(lines)):
    heapq.heappush(freq, (int(lines[i]), [i]))

T = [[] for i in range(0, len(lines))]


def merge(a, b):
    new = deepcopy(a[1])
    new.extend(b[1])
    return a[0] + b[0], new


while len(freq) > 1:
    a = heapq.heappop(freq)
    b = heapq.heappop(freq)
    ab = merge(a, b)
    for i in a[1]:
        T[i].append(0)
    for j in b[1]:
        T[j].append(1)
    heapq.heappush(freq, ab)

L = []
for node in T:
    L.append(len(node))

print(min(L))
print(max(L))