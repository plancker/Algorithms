import math
import heapq

file = open("nn.txt", "r")
lines = file.readlines()
num_nodes = int(lines[0])
points = [(0, 0)]
distances = [{} for i in range(num_nodes+1)]
for line in lines[1:]:
    x = float(line.split()[1])
    y = float(line.split()[2])
    points.append((x, y))


# point_set = list(range(1, num_nodes+1))

def dist(v, w):
    return (v[0]-w[0])**2+(v[1]-w[1])**2


# distances = [[] for i in range(0, num_nodes+1)]

# for v in points:
#     for w in points:
#         if v != w:
#             heapq.heappush(distances[v], (dist(v, w), w))




# LARGE = 10000000


# def dijkstra(source):
#     Seen = [source]
#     Not_Seen = list(range(1, source))
#     Not_Seen.extend(list(range(source+1, num_nodes+1)))
#     DGS = 0
#     # DGS[source] = 0
#     while Not_Seen:
#         min_score_edge = [LARGE, 0]
#         v = Seen[len(Seen)-1]
#         Pop_this = None
#         for i in range(0, len(Not_Seen)):
#             w = Not_Seen[i]
#             dgs = dist(points[v], points[w])
#             print(len(Not_Seen))
#             if dgs < min_score_edge[0]:
#                 e = [dgs, w]
#                 min_score_edge = e
#                 Pop_this = i
#         newcomer = min_score_edge[1]
#         Not_Seen.pop(Pop_this)
#         DGS = DGS + math.sqrt(min_score_edge[0])
#         Seen.append(newcomer)
#     return DGS, Seen[len(Seen)-1]


def dijkstra(source):
    Seen = [source]
    Not_Seen = list(range(1, source))
    Not_Seen.extend(list(range(source+1, num_nodes+1)))
    DGS = 0
    # DGS[source] = 0
    while Not_Seen:
        v = Seen[len(Seen)-1]
        New_Not_Seen = sorted(Not_Seen, key=lambda x: dist(points[x], points[v]))
        if len(Not_Seen) > 2:
            if New_Not_Seen[0] > New_Not_Seen[1] and dist(points[v], points[New_Not_Seen[1]]) == dist(points[v], points[New_Not_Seen[0]]):
                print("Oops")
        print(len(Not_Seen))
        dgs = dist(points[v], points[New_Not_Seen[0]])
        Not_Seen.remove(New_Not_Seen[0])
        DGS = DGS + math.sqrt(dgs)
        Seen.append(New_Not_Seen[0])
    return DGS, Seen[len(Seen)-1]


# def sum_elements(arr):
#     m_sum = 0
#     for i in arr:
#         m_sum = m_sum + i
#     return m_sum


Output = dijkstra(1)
print(Output)
print(Output[0]+math.sqrt(dist(points[Output[1]], points[1])))