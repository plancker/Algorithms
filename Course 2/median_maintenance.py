import heapq
file = open("Median.txt", "r")
r_data = file.readlines()
data = [int(x) for x in r_data]
print(data)


medians = []


k = 0
l_heap = []
u_heap = []

while k < len(data):
    new = data[k]
    l_max = 0
    u_min = 0

    if len(l_heap) > 0:
        l_max = l_heap[0][1]

    if len(u_heap) > 0:
        u_min = u_heap[0]

    if new > l_max:
        heapq.heappush(u_heap, new)
    else:
        heapq.heappush(l_heap, (-new, new))

    diff = len(l_heap) - len(u_heap)

    if diff > 1:
        x = heapq.heappop(l_heap)[1]
        heapq.heappush(u_heap, x)
    elif diff < -1:
        x = heapq.heappop(u_heap)
        heapq.heappush(l_heap, (-x, x))

    median = None

    diff = len(l_heap) - len(u_heap)

    if (k+1) % 2 == 0 and diff == 0:
        median = l_heap[0][1]
    elif (k+1) % 2 == 1 and diff == 1:
        median = l_heap[0][1]
    elif (k+1) % 2 == 1 and diff == -1:
        median = u_heap[0]
    else:
        print("Something bad happened", l_heap, u_heap)

    medians.append(median)

    k = k + 1


sum = 0

for t in range(0, 10000):
    sum = sum + medians[t]

print(sum % 10000)




