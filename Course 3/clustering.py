file = open("clustering.txt", "r")
lines = file.readlines()
num_nodes = 500
edges = []
distances = [{} for i in range(0, num_nodes+1)]
for line in lines:
    items = line.split()
    e = [int(i) for i in items]
    distances[int(items[0])][int(items[1])] = int(items[2])
    distances[int(items[1])][int(items[0])] = int(items[2])
    edges.append(e)

edges.sort(key=lambda x: x[2])

C = [[i] for i in range(0, num_nodes+1)]

No_clusters = num_nodes


def size(leader_vertex):
    return len(C[leader_vertex])


def merge(big_c_leader, small_c_leader):
    C[big_c_leader].extend(C[small_c_leader])
    for i in C[small_c_leader]:
        C[i] = [big_c_leader]


def leader(v):
    return C[v][0]


for e in edges:
    if No_clusters > 4:
        v1 = e[0]
        v2 = e[1]
        v1_leader = leader(v1)
        v2_leader = leader(v2)
        if size(v1_leader) > size(v2_leader):
            merge(v1_leader, v2_leader)
            No_clusters = No_clusters - 1
        elif size(v1_leader) < size(v2_leader):
            merge(v2_leader, v1_leader)
            No_clusters = No_clusters - 1
        elif size(v1_leader) == size(v2_leader):
            if v1_leader == v2_leader:
                pass
            else:
                merge(v1_leader, v2_leader)
                No_clusters = No_clusters - 1

# for e in edges:
#     leaders = []
#     if leader(e[0]) not in leaders:
#         leaders.append(leader(e[0]))
#     if leader(e[1]) not in leaders:
#         leaders.append(leader(e[1]))
#

    # if leader(e[0]) != leader(e[1]):
    #     print(e, leader(e[0]), leader(e[1]))

C = [C[x] for x in range(1, len(C)) if C[x][0] == x]

print(C)
d_Clusters = [{} for i in range(0, 4)]


def cluster_dist(A, B):
    d = 10000000
    for a in A:
        for b in B:
            if b in distances[a]:
                if distances[a][b] < d:
                    d = distances[a][b]
    return d


spacing = 10000000
for i in range(0, len(C)):
    for j in range(i+1, len(C)):
        if cluster_dist(C[i], C[j]) < spacing:
            spacing = cluster_dist(C[i], C[j])

print(spacing)
