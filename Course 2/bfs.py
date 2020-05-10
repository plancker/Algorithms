num_nodes = 13
file = open("../Course 4/test.txt", "r")
lines = file.readlines()
graph = [[] for i in range(num_nodes)]
for line in lines:
    items = line.split()
    graph[int(items[0])].append(int(items[1]))


visited = [False]*num_nodes


def bfs(g, start, end):
    queue = [start]
    parent = [None]*num_nodes
    visited[start] = True
    while queue:
        head = queue[0]
        for v in g[head]:
            if not visited[v]:
                queue.append(v)
                parent[v] = head
                visited[v] = True
                if v == end:
                    break
        queue.pop(0)

    if parent[end]:
        r_path = [end]

        def get_ancestors(current):
            if current == start:
                return r_path
            else:
                r_path.append(parent[current])
                get_ancestors(parent[current])

        get_ancestors(end)

        r_path.reverse()

        return r_path

    else:
        return "No path found"


print(bfs(graph, 12, 11))


