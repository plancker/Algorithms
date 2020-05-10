# returns answer only for distinct numbers
def calculate_largest(unsorted_array):
    if len(unsorted_array) == 2:
        if unsorted_array[0] > unsorted_array[1]:
            return unsorted_array[0]
        else:
            return unsorted_array[1]
    elif len(unsorted_array) == 1:
        return unsorted_array[0]
    else:
        a = calculate_largest(unsorted_array[:len(unsorted_array) // 2])
        b = calculate_largest(unsorted_array[len(unsorted_array) // 2:])
        if a > b:
            return a
        else:
            return b


print(calculate_largest([35, 1, 333, 23]))


def calculate_largest_2(unsorted_array):
    largest = unsorted_array[0]
    second_largest = unsorted_array[0]
    for i in range(0, len(unsorted_array)):
        if unsorted_array[i + 1] > largest:
            largest = unsorted_array[i + 1]
            second_largest = unsorted_array[i]
    return largest

print(calculate_largest([35,1,2,3456,23,445]))

def calculate_second_largest(unsorted_array):
