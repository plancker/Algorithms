num_nodes = 201
file = open("dijkstraData.txt", "r")
lines = file.readlines()
data = [None] * num_nodes
for line in lines:
    if line.strip():
        items = line.split()
        d = dict()
        for i in items[1:]:
            pair = i.split(",")
            d[int(pair[0])] = int(pair[1])
        data[int(items[0])] = d

print(data)


source = 1
LARGE = 1000000


def dist(a, b):
    return data[a][b]


def dijkstra():
    Seen = [source]
    Not_Seen = list(range(0, source))
    Not_Seen.extend(list(range(source+1, num_nodes)))
    DGS = [LARGE]*num_nodes
    DGS[source] = 0
    while Not_Seen:
        min_score_edge = [LARGE, 0, 0]
        for v in Seen:
            for w in Not_Seen:
                if w in data[v].keys():
                    dgs = dist(v, w) + DGS[v]
                    if dgs < min_score_edge[0]:
                        e = [dgs, v, w]
                        min_score_edge = e
        newcomer = min_score_edge[2]
        Not_Seen.remove(newcomer)
        DGS[newcomer] = min_score_edge[0]
        Seen.append(newcomer)
    return DGS

path_lengths = dijkstra()
Vertices = [7,37,59,82,99,115,133,165,188,197]
output = []
for i in Vertices:
    output.append(path_lengths[i])
print(output)