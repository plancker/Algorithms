import heapq
file = open("prims.txt", "r")
lines = file.readlines()
num_nodes = int(lines[0].split()[0])
num_edges = int(lines[0].split()[1])
edges_from_vertex = [dict() for i in range(num_nodes+1)]
for line in lines[1:]:
    items = line.split()
    v = int(items[0])
    w = int(items[1])
    c = int(items[2])
    edges_from_vertex[v][w] = c
    edges_from_vertex[w][v] = c
print(edges_from_vertex)

source = 1
LARGE = 100000000000000000000


def prims_mst():
    Seen = [source]
    Not_Seen = list(range(1, source))
    Not_Seen.extend(list(range(source+1, num_nodes+1)))
    print(Not_Seen)
    total_cost = 0
    while Not_Seen:
        min_score_edge = [LARGE, 0, 0]
        for v in Seen:
            for w in Not_Seen:
                if w in edges_from_vertex[v].keys():
                    cost = edges_from_vertex[v][w]
                    if cost < min_score_edge[0]:
                        e = [cost, v, w]
                        min_score_edge = e
        newcomer = min_score_edge[2]
        Not_Seen.remove(newcomer)
        total_cost = total_cost + min_score_edge[0]
        Seen.append(newcomer)
    return total_cost

print(prims_mst())




