# Mapping 2SAT to DFS

# x or y is equivalent to if not x then y and if not y then x. Now, we make an edge between x and y if
# x implies y. In this way if x and not x are in the same SCC, then we have x implies not x which means the
# assignment isn't satisfiable.

file = open("2sat6.txt", "r")
data = file.readlines()
num_clauses = int(data[0])
num_vars = num_clauses
num_nodes = num_clauses+1

graph = {i: set() for i in range(-num_nodes+1, num_nodes)}
r_graph = {i: set() for i in range(-num_nodes+1, num_nodes)}

visited = {i: False for i in range(-num_nodes+1, num_nodes)}
total_visited = 0

scc = {i: 0 for i in range(-num_nodes+1, num_nodes)}

stack = []
order = []

# (1+4) -> 3
# (3+4) -> 1
# 1 -> 4
# (4+4) -> (1+4)
# 3 -> 4
# (4+4) -> (4+3)
# (4+4) -> (4+1)
# 1 -> 4


def neg(x):
    if x < 0:
        return num_clauses + x
    else:
        return x - num_clauses - 1


for line in data[1:]:
    items = line.split()
    graph[-1*int(items[0])].add(int(items[1]))
    graph[-1*int(items[1])].add(int(items[0]))
    r_graph[int(items[1])].add(-1*int(items[0]))
    r_graph[int(items[0])].add(-1*int(items[1]))

# print(graph)
# print(r_graph)

# DFS on reverse graph
for node in reversed(range(-num_nodes+1, num_nodes)):
    if not visited[node] and node != 0:
        stack = [node]
        visited[node] = True
        while stack:
            stack_node = stack[len(stack)-1]
            if len(r_graph[stack_node])>0:
                for head in r_graph[stack_node]:
                    if not visited[head]:
                        stack.append(head)
                        visited[head] = True
                        total_visited = total_visited+1
                    elif len(stack) > 0 and stack[len(stack)-1] == stack_node:
                        order.append(stack_node)
                        stack.pop()
            else:
                order.append(stack_node)
                stack.pop()

# print(order)

# DFS on original graph

visited = {i: False for i in range(-num_nodes+1, num_nodes)}

order.reverse()

scc_no = 0

for node in order:
    if not visited[node] and node != 0:
        stack = [node]
        visited[node] = True
        while stack:
            stack_node = stack[len(stack)-1]
            scc[stack_node] = scc_no
            if len(graph[stack_node]) > 0:
                for head in graph[stack_node]:
                    if not visited[head]:
                        stack.append(head)
                        visited[head] = True
                    elif len(stack) > 0 and stack[len(stack)-1] == stack_node:
                        stack.pop()
            else:
                stack.pop()

        scc_no = scc_no+1



# Getting the five biggest sccs
# scc.sort(reverse=True)

for i in range(1, num_nodes):
    if scc[-i] == scc[i]:
        print("No can't do!", i)
# print(scc)
# print(scc)



