def merge_sort(list_to_sort):
    length_of_list = len(list_to_sort)
    sorted_list = list()
    if length_of_list == 2:
        if list_to_sort[0] > list_to_sort[1]:
            sorted_list.append(list_to_sort[1])
            sorted_list.append(list_to_sort[0])
        else:
            sorted_list = list_to_sort
        return sorted_list
    elif length_of_list == 1:
        return list_to_sort
    else:
        list_to_sort_part1 = list_to_sort[0:int(length_of_list / 2)]
        list_to_sort_part2 = list_to_sort[int(length_of_list / 2):length_of_list]
        sorted_list_part1 = merge_sort(list_to_sort_part1)
        sorted_list_part2 = merge_sort(list_to_sort_part2)
        i = 0
        j = 0
        for k in range(0,length_of_list):
            if i <= len(sorted_list_part1)-1 and j <= len(sorted_list_part2)-1:
                if sorted_list_part1[i] > sorted_list_part2[j]:
                    sorted_list.append(sorted_list_part2[j])
                    j = j + 1
                else:
                    sorted_list.append(sorted_list_part1[i])
                    i = i + 1
            elif i <= len(sorted_list_part1)-1:
                sorted_list.extend(sorted_list_part1[i:len(sorted_list_part1)])
                i = len(sorted_list_part1)
            else:
                sorted_list.extend(sorted_list_part2[j:len(sorted_list_part2)])
                j = len(sorted_list_part2)

        return sorted_list


print(merge_sort([332232, 200, 11, 4123, 544,92,133,45,6,7,890,1]))
