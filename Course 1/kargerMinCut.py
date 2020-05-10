from random import randint
import copy


def karger_min_cut(graph):
    rows = copy.deepcopy(graph)

    def combine_adjacency_lists(v_a_adjacent, v_b_adjacent):
        if isinstance(v_a_adjacent[0], int) and isinstance(v_b_adjacent[0], int):
            new_vertex = [v_a_adjacent[0], v_b_adjacent[0]]
            connected_points_to_a = [x for x in v_a_adjacent[1:] if x not in new_vertex]
            connected_points_to_b = [x for x in v_b_adjacent[1:] if x not in new_vertex]
            new_vertex_adjacent = [new_vertex]
            new_vertex_adjacent.extend(connected_points_to_a)
            new_vertex_adjacent.extend(connected_points_to_b)
            return new_vertex_adjacent
        elif isinstance(v_a_adjacent[0], list) and isinstance(v_b_adjacent[0], int):
            new_vertex = copy.deepcopy(v_a_adjacent[0])
            new_vertex.append(v_b_adjacent[0])
            connected_points_to_a = [x for x in v_a_adjacent[1:] if x not in new_vertex]
            connected_points_to_b = [x for x in v_b_adjacent[1:] if x not in new_vertex]
            new_vertex_adjacent = [new_vertex]
            new_vertex_adjacent.extend(connected_points_to_a)
            new_vertex_adjacent.extend(connected_points_to_b)
            return new_vertex_adjacent
        elif isinstance(v_a_adjacent[0], list) and isinstance(v_b_adjacent[0], list):
            new_vertex = copy.deepcopy(v_a_adjacent[0])
            new_vertex.extend(v_b_adjacent[0])
            connected_points_to_a = [x for x in v_a_adjacent[1:] if x not in new_vertex]
            connected_points_to_b = [x for x in v_b_adjacent[1:] if x not in new_vertex]
            new_vertex_adjacent = [new_vertex]
            new_vertex_adjacent.extend(connected_points_to_a)
            new_vertex_adjacent.extend(connected_points_to_b)
            return new_vertex_adjacent
        elif isinstance(v_a_adjacent[0], int) and isinstance(v_b_adjacent[0], list):
            return combine_adjacency_lists(v_b_adjacent, v_a_adjacent)

    def get_row_index_of_vertex(vertex, adjacency_lists):
        for t in range(0, len(adjacency_lists)):
            if isinstance(adjacency_lists[t][0], int):
                if vertex == adjacency_lists[t][0]:
                    return t
            elif isinstance(adjacency_lists[t][0], list):
                for m in range(0, len(adjacency_lists[t][0])):
                    if vertex == adjacency_lists[t][0][m]:
                        return t

    while len(rows) > 2:
        v_a_index = randint(1, len(rows)) - 1
        v_a_adjacent = rows[v_a_index]
        v_b_index_in_a_list = randint(2, len(v_a_adjacent)) - 1
        v_b = v_a_adjacent[v_b_index_in_a_list]
        v_b_index = get_row_index_of_vertex(v_b, rows)
        v_b_adjacent = rows[v_b_index]
        rows[v_a_index] = combine_adjacency_lists(v_a_adjacent, v_b_adjacent)
        rows.pop(v_b_index)

    return rows


def calculate_min_cut(graph):
    mincuts = []
    for k in range(0, 200):
        partition = karger_min_cut(graph)
        if isinstance(partition[0][0], list):
            mincuts.append(len(partition[0]) - 1)
        elif isinstance(partition[1][0], list):
            mincuts.append(len(partition[1]) - 1)
    print(min(mincuts))


graph_file = open("kargerMinCut.text", "r")
graph = graph_file.read().split("\n")
for i in range(0, len(graph)):
    row = graph[i].split("\t")
    graph[i] = list(map(int, row[0:len(row) - 1]))

calculate_min_cut(graph)
