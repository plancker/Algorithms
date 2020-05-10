file = open("jobs.txt", "r")
lines = file.readlines()
num_nodes = int(lines[0])

jobs = [[] for x in range(num_nodes)]


def score(v):
    sc = v[1]/v[0]
    return sc


for i in range(1, num_nodes+1):
    attbs = [int(t) for t in lines[i].split()]
    attbs.append(score(attbs))
    jobs[i-1].extend(attbs)

jobs.sort(key=score)


# Resolving Ties
i = 0
while i < len(jobs)-1:
    a = jobs[i]
    b = jobs[i+1]
    if a[2] == b[2]:
        if b[0] > a[0]:
            temp = jobs[i+1]
            jobs[i+1] = jobs[i]
            jobs[i] = temp
    i = i + 1


print(jobs)

# Calculating completion time sum

comp_sum = 0
t = 0
j = 0
while j < len(jobs):
    t = t + jobs[j][1]
    comp_sum = comp_sum + jobs[j][0]*t
    j = j+1

print(comp_sum)




# source = 1
# LARGE = 1000000
#
#
# def schedule():
#     Seen = [source]
#     Not_Seen = list(range(0, source))
#     Not_Seen.extend(list(range(source+1, num_nodes)))
#     DGS = [LARGE]*num_nodes
#     DGS[source] = 0
#     while Not_Seen:
#         min_score_job = [LARGE, 0, 0]
#         for v in Seen:
#             for w in Not_Seen:
#                 if w in data[v].keys():
#                     dgs = dist(v, w) + DGS[v]
#                     if dgs < min_score_edge[0]:
#                         e = [dgs, v, w]
#                         min_score_edge = e
#         newcomer = min_score_edge[2]
#         Not_Seen.remove(newcomer)
#         DGS[newcomer] = min_score_edge[0]
#         Seen.append(newcomer)
#     return DGS
