import math
import itertools

file = open("tsp.txt", "r")
lines = file.readlines()
num_nodes = int(lines[0])
points = [(0, 0)]
distances = [{} for i in range(num_nodes+1)]
for line in lines[1:]:
    x = float(line.split()[0])
    y = float(line.split()[1])
    points.append((x, y))

point_set = list(range(1, num_nodes+1))


# def powerset(max_len):
#
#     def sum_digits(n):
#         r = 0
#         while n:
#             r, n = r + n % 10, n // 10
#         return r
#
#     all_str = ["".join(seq) for seq in itertools.product("01", repeat=max_len)]
#
#     hash_table = [{} for i in range(0, max_len+1)]
#
#     processed = 0
#
#     for my_str in all_str:
#         hash_table[sum_digits((int(my_str)))][my_str] = my_str
#         processed = processed + 1
#         print(processed)
#
#     return hash_table


# MAIN_TABLE = powerset(num_nodes)


# print(len(MAIN_TABLE))


def kbits(n, k):
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return result


for i in range(1, len(points)):
    for j in range(1, len(points)):
        if i != j:
            v = points[i]
            w = points[j]
            distances[i][j] = math.sqrt((v[0]-w[0])**2+(v[1]-w[1])**2)

print(distances)

A = {}
LARGE = 1000000


for i in range(1, len(points)):
    valid_sets = kbits(num_nodes, i)
    T = {}
    print("i = ", i)
    k = 0
    for s in valid_sets:
        if int(s[0]) == 1:
            T[s] = {}
            for j in [t+1 for t in range(0, num_nodes) if int(s[t]) == 1]:
                if j != 1:
                    S_without_j_key = s[:j-1]+"0"+s[j:]
                    X = [t+1 for t in range(0, num_nodes) if int(S_without_j_key[t]) == 1]
                    T[s][j] = min([A[S_without_j_key][k] + distances[k][j] for k in X])
                else:
                    if s == "1"+"0"*(num_nodes-1):
                        T[s][j] = 0
                    else:
                        T[s][j] = LARGE
        k = k + 1
        print(k/len(valid_sets), i)
    A = T
    # print("A", len(A))


print(min([A["1"*num_nodes][j] + distances[j][1] for j in list(range(2, num_nodes+1))]))
