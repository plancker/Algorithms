# Data Structures

num_nodes = 13

graph = [[] for i in range(num_nodes)]
r_graph = [[] for i in range(num_nodes)]

visited = [False] * num_nodes
total_visited = 0

scc = [0] * num_nodes

stack = []
order = []

# Importing the graphs

file = open("../Course 4/test.txt", "r")
data = file.readlines()

for line in data:
    items = line.split()
    graph[int(items[0])].append(int(items[1]))
    r_graph[int(items[1])].append(int(items[0]))

print("graph and r_graph created")

# DFS on reverse graph
for node in reversed(range(num_nodes)):
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

print(order)

# DFS on original graph

visited = [False] * len(visited)

order.reverse()

scc_no = 0

for node in order:
    if not visited[node] and node != 0:
        stack = [node]
        visited[node] = True
        while stack:
            stack_node = stack[len(stack)-1]
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
scc.sort(reverse=True)
print(scc[:5])



