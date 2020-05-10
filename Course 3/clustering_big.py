def getbase2(l):
    # Converting integer list to string list
    s = [str(i) for i in l]
    # Join list items using join()
    res = int(("".join(s)), 2)
    return res


file = open("clustering_big.txt", "r")
lines = file.readlines()
num_nodes = len(lines)
hash_table = {}

for line in lines:
    arr = line.split()
    string = line.replace(" ", "")
    int_val = int(string, 2)
    if int_val not in hash_table.keys():
        hash_table[int_val] = [[int(i) for i in line.split()], False]


def points_within_dist(v1, d):
    arr = []
    if d == 1:
        for i in range(0, len(v1)):
            if v1[i] == 1:
                n = v1[0:i]
                n.extend([0])
                n.extend(v1[i+1:])
            else:
                n = v1[0:i]
                n.extend([1])
                n.extend(v1[i+1:])
            arr.append(n)
        return arr
    elif d == 2:
        for i in range(0, len(v1)):
            for j in range(i, len(v1)):
                if i != j:
                    if i < j:
                        if v1[i] == 1 and v1[j] == 1:
                            n = v1[0:i]
                            n.extend([0])
                            n.extend(v1[i+1:j])
                            n.extend([0])
                            n.extend(v1[j+1:len(v1)])
                        elif v1[i] == 0 and v1[j] == 1:
                            n = v1[0:i]
                            n.extend([1])
                            n.extend(v1[i+1:j])
                            n.extend([0])
                            n.extend(v1[j+1:len(v1)])
                        elif v1[i] == 1 and v1[j] == 0:
                            n = v1[0:i]
                            n.extend([0])
                            n.extend(v1[i+1:j])
                            n.extend([1])
                            n.extend(v1[j+1:len(v1)])
                        else:
                            n = v1[0:i]
                            n.extend([1])
                            n.extend(v1[i+1:j])
                            n.extend([1])
                            n.extend(v1[j+1:len(v1)])
                        arr.append(n)
        return arr


print(len(hash_table.keys()))


C = {v_hash: [v_hash] for v_hash in hash_table.keys()}


No_clusters = len(hash_table.keys())


def size(leader_vertex):
    return len(C[leader_vertex])


def merge(big_c_leader, small_c_leader):
    C[big_c_leader].extend(C[small_c_leader])
    for i in C[small_c_leader]:
        C[i] = [big_c_leader]


def leader(v):
    return C[v][0]


for v1_hash in hash_table.keys():
    v1_visited = hash_table[v1_hash][1]
    # if not v1_visited:
    points_in_reach = points_within_dist(hash_table[v1_hash][0], 1)
    points_in_reach.extend(points_within_dist(hash_table[v1_hash][0], 2))
    for j in range(0, len(points_in_reach)):
        v2 = points_in_reach[j]
        v2_hash = getbase2(v2)
        if v2_hash in hash_table.keys():
            v2_visited = hash_table[v2_hash][1]
            # if not v2_visited:
            v1_leader = leader(v1_hash)
            v2_leader = leader(v2_hash)
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
            hash_table[v1_hash][1] = True
            hash_table[v2_hash][1] = True
            print(No_clusters)



