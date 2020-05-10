def count_inversions(my_list, total_inversions):
    length_of_list = len(my_list)
    sorted_list = list()
    if length_of_list == 2:
        if my_list[0] > my_list[1]:
            sorted_list.append(my_list[1])
            sorted_list.append(my_list[0])
            total_inversions = total_inversions + 1
            return sorted_list, total_inversions
        else:
            sorted_list = my_list
        return sorted_list, total_inversions
    elif length_of_list == 1:
        return my_list, total_inversions
    else:
        list_to_sort_part1 = my_list[0:int(length_of_list / 2)]
        list_to_sort_part2 = my_list[int(length_of_list / 2):length_of_list]
        sorted_list_part1 = count_inversions(list_to_sort_part1, total_inversions)
        sorted_list_part1_array = sorted_list_part1[0]
        sorted_list_part1_inversions = sorted_list_part1[1]
        sorted_list_part2 = count_inversions(list_to_sort_part2, total_inversions)
        sorted_list_part2_array = sorted_list_part2[0]
        sorted_list_part2_inversions = sorted_list_part2[1]
        total_inversions = total_inversions + sorted_list_part1_inversions + sorted_list_part2_inversions
        i = 0
        j = 0
        for k in range(0, length_of_list):
            if i <= len(sorted_list_part1_array) - 1 and j <= len(sorted_list_part2_array) - 1:
                if sorted_list_part1_array[i] > sorted_list_part2_array[j]:
                    sorted_list.append(sorted_list_part2_array[j])
                    j = j + 1
                    total_inversions = total_inversions + len(sorted_list_part1_array) - len(sorted_list_part1_array[0:i])
                else:
                    sorted_list.append(sorted_list_part1_array[i])
                    i = i + 1
            elif i <= len(sorted_list_part1_array) - 1:
                sorted_list.extend(sorted_list_part1_array[i:len(sorted_list_part1_array)])
                i = len(sorted_list_part1_array)
                total_inversions = total_inversions + len(sorted_list_part1_array[i:len(sorted_list_part1_array)])
            else:
                sorted_list.extend(sorted_list_part2_array[j:len(sorted_list_part2_array)])
                j = len(sorted_list_part2_array)
        return sorted_list, total_inversions


integer_list_file = open("PA2_Integer_Array.txt", "r")
integer_list = integer_list_file.read().split("\n")
integer_list = list(map(int, integer_list))
print(integer_list)
print(count_inversions(integer_list, 0)[1])
