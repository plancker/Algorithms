def choose_pivot(list_to_sort):
    return 0


def swap_in_array(array, id1, id2):
    temp = array[id2]
    array[id2] = array[id1]
    array[id1] = temp


def quick_sort(list_to_sort, starting_id, ending_id, comparisons):
    length_of_list = ending_id - starting_id
    if length_of_list == 2:
        if list_to_sort[ending_id - 1] < list_to_sort[starting_id]:
            swap_in_array(list_to_sort, ending_id - 1, starting_id)
            return list_to_sort, 1
        else:
            return list_to_sort, 1
    elif length_of_list <= 1:
        return list_to_sort, 0
    else:
        swap_in_array(list_to_sort, starting_id, ending_id - 1)
        pivot_id = starting_id
        partition_id = pivot_id + 1
        for j in range(partition_id, ending_id):
            if list_to_sort[j] < list_to_sort[pivot_id]:
                swap_in_array(list_to_sort, partition_id, j)
                partition_id = partition_id + 1
        swap_in_array(list_to_sort, pivot_id, partition_id - 1)
        # list_to_sort_part1 = list_to_sort[0:int(length_of_list / 2)]
        # list_to_sort_part2 = list_to_sort[int(length_of_list / 2):length_of_list]
        # [2, 4, 1, 3] -> [2, 4, 1, 3] -> [2, 1, 4, 3] -> [2, 1, 4 , 3]
        comparisons = comparisons + quick_sort(list_to_sort, starting_id, partition_id - 1, comparisons)[1] + \
                      quick_sort(list_to_sort, partition_id, ending_id, comparisons)[1]
        comparisons = comparisons + length_of_list - 1

        return list_to_sort, comparisons


def quick_sort_with_median(list_to_sort, starting_id, ending_id, comparisons):
    my_list = list_to_sort[starting_id:ending_id]
    length_of_list = ending_id - starting_id
    if length_of_list == 2:
        if list_to_sort[ending_id - 1] < list_to_sort[starting_id]:
            swap_in_array(list_to_sort, ending_id - 1, starting_id)
            return list_to_sort, 1
        else:
            return list_to_sort, 1
    elif length_of_list <= 1:
        return list_to_sort, 0
    else:
        if length_of_list%2 == 0:
            middle_id = starting_id + length_of_list//2 - 1
        else:
            middle_id = starting_id + (length_of_list-1)//2
        if (list_to_sort[starting_id] < list_to_sort[middle_id] < list_to_sort[ending_id-1]) or (list_to_sort[ending_id-1] < list_to_sort[middle_id] < list_to_sort[starting_id]):
            swap_in_array(list_to_sort, starting_id, middle_id)
        elif (list_to_sort[middle_id] < list_to_sort[starting_id] < list_to_sort[ending_id-1]) or (list_to_sort[ending_id-1] < list_to_sort[starting_id] < list_to_sort[middle_id]):
            swap_in_array(list_to_sort, starting_id, starting_id)
        else:
            swap_in_array(list_to_sort, starting_id, ending_id-1)
        pivot_id = starting_id
        partition_id = pivot_id + 1
        for j in range(partition_id, ending_id):
            if list_to_sort[j] < list_to_sort[pivot_id]:
                swap_in_array(list_to_sort, partition_id, j)
                partition_id = partition_id + 1
        swap_in_array(list_to_sort, pivot_id, partition_id - 1)
        # list_to_sort_part1 = list_to_sort[0:int(length_of_list / 2)]
        # list_to_sort_part2 = list_to_sort[int(length_of_list / 2):length_of_list]
        # [2, 4, 1, 3] -> [2, 4, 1, 3] -> [2, 1, 4, 3] -> [2, 1, 4 , 3]
        comparisons = comparisons + quick_sort_with_median(list_to_sort, starting_id, partition_id - 1, comparisons)[
            1] + quick_sort_with_median(list_to_sort, partition_id, ending_id, comparisons)[1]
        comparisons = comparisons + length_of_list - 1

        return list_to_sort, comparisons


integer_list_file = open("PA3_Integer_Array.txt", "r")
integer_list = integer_list_file.read().split("\n")
integer_list = list(map(int, integer_list))
# integer_list = [3, 8, 2, 5, 1, 4, 7, 6]
#print("list = ", integer_list)
#print(quick_sort(integer_list, 0, len(integer_list), 0)[1])
print(quick_sort_with_median(integer_list, 0, len(integer_list), 0)[1])
