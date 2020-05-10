import copy
file = open("g3.txt", "r")
lines = file.readlines()
num_nodes = int(lines[0].split()[0])
num_edges = int(lines[0].split()[1])

in_edge = [{} for i in range(num_nodes + 1)]
g = [{} for i in range(num_nodes + 1)]
g_new = [{} for i in range(num_nodes + 1)]

for line in lines[1:]:
    items = line.split()
    a1 = int(items[0])
    a2 = int(items[1])
    wgt = int(items[2])
    if a1 in in_edge[a2].keys():
        in_edge[a2][a1] = min(wgt, in_edge[a2][a1])
    else:
        in_edge[a2][a1] = wgt
    if a2 in g[a1].keys():
        g[a1][a2] = min(wgt, g[a1][a2])
    else:
        g[a1][a2] = wgt

LARGE = 100000


def bellman(source):
    n = len(g)
    sd = [LARGE]*n
    sd[source] = 0
    for v in g[source].keys():
        sd[v] = g[source][v]
    for i in range(1, n):
        X = copy.deepcopy(sd)
        for v in range(1, n):
            possible_w = list(in_edge[v].keys())
            if len(possible_w) > 0:
                sd[v] = min(X[v], min([X[w] + g[w][v] for w in possible_w]))
            else:
                sd[v] = X[v]
            if i == num_nodes+1 and sd[v] != X[v]:
                return None
    return sd


def dist(a, b):
    d = g[a][b]
    return d


def dijkstra(source):
    print(source)
    Seen = [source]
    Not_Seen = list(range(1, source))
    Not_Seen.extend(list(range(source + 1, num_nodes + 1)))
    DGS = [LARGE] * (num_nodes + 1)
    DGS[source] = 0
    prog = len(Seen)
    while len(Seen) < num_nodes+1:
        min_score_edge = [LARGE, 0, 0]
        for v in Seen:
            min_edges = {}
            for w in g[v].keys():
                dgs = dist(v, w) + DGS[v]
                if w in Not_Seen or dgs < DGS[w]:
                    e = [dgs, v, w]
                    if dgs in min_edges.keys():
                        min_edges[dgs].append(e)
                    else:
                        min_edges[dgs] = [e]
                    if dgs < min_score_edge[0]:
                        min_score_edge = e
            if len(min_edges.keys()) > 0 and len(Not_Seen)>0:
                for e in min_edges[min_score_edge[0]]:
                    newcomer = e[2]
                    if newcomer in Not_Seen:
                        Not_Seen.remove(newcomer)
                    DGS[newcomer] = e[0]
                    Seen.append(newcomer)
            min_score_edge = [LARGE, 0, 0]
        if prog == len(Seen):
            break
        else:
            prog = len(Seen)
    return DGS


def reweigh_edges(vertex_weights):
    for v in range(1, len(g)-1):
        for w in g[v].keys():
            g[v][w] = g[v][w] + vertex_weights[v] - vertex_weights[w]


def johnson():
    s = {v: 0 for v in range(1, num_nodes + 1)}
    g.append(s)
    in_edge.append({})
    Short_Dists = bellman(len(g) - 1)
    if Short_Dists is not None:
        print(min(Short_Dists))
        # g.pop()
        # reweigh_edges(Short_Dists)
        # Distances = [0]*(num_nodes+1)
        # min_dist = LARGE
        # blah = 0
        # blah_blah = [4, 15, 34, 47, 53, 68, 70, 73, 87, 103, 124, 155, 172, 188, 225, 227, 236, 252]
        # for t in range(0, len(blah_blah)-1):
        #     blah = blah + (g[blah_blah[t]][blah_blah[t+1]]-Short_Dists[blah_blah[t]]+Short_Dists[blah_blah[t+1]])
        # print("blah", blah)
        # for i in range(1, num_nodes+1):
        #     Distances[i] = dijkstra(i)
        # for i in range(1, len(Distances)):
        #     for j in range(1, len(Distances[i])):
        #         Distances[i][j] = Distances[i][j] - Short_Dists[i] + Short_Dists[j]
        #         if i != j and Distances[i][j] < min_dist:
        #             min_dist = Distances[i][j]
        # print(min_dist)
    else:
        print("Negative Cycle Found")


johnson()