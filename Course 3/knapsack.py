import sys
sys.setrecursionlimit(10**6)
file = open("knapsack_big.txt", "r")
lines = file.readlines()
Capacity = int(lines[0].split()[0])
Num_items = int(lines[0].split()[1])
items = [[0, 0]]
items.extend([int(line.split()[0]), int(line.split()[1])] for line in lines[1:])

A = [{} for i in range(Num_items+1)]


def knapsack(i, cap):
    if cap in A[i].keys():
        return A[i][cap]
    elif cap in A[i-1].keys() and cap-items[i][1] in A[i-1].keys():
        A[i][cap] = max(A[i-1][cap], A[i-1][cap-items[i][1]]+items[i][0])
        return A[i][cap]
    else:
        if i > 1 and cap > 1:
            if cap > items[i][1]-1:
                val = max(knapsack(i-1, cap), knapsack(i-1, cap - items[i][1])+items[i][0])
                A[i][cap] = val
            else:
                val = knapsack(i-1, cap)
                A[i][cap] = val
            return val
        else:
            A[i][cap] = 0
            return 0

print(knapsack(Num_items, Capacity))

# for i in range(1, Num_items+1):
#     B = [0 for i in range(Capacity+1)]
#     for c in range(0, Capacity+1):
#         if c > items[i][1]-1:
#             B[c] = max(A[c], A[c-items[i][1]]+items[i][0])
#         else:
#             B[c] = A[c]
#     A = B
#     print(i, c)
#
# fin_arr = A[len(A)-1]
# print(fin_arr)

# 2493893

