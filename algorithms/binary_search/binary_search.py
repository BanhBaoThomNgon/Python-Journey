import math

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1
    while begin_index <= end_index:
        midpoint = math.floor((end_index - begin_index)/2) + begin_index
        midpoint_value = sequence[midpoint]
        if (sequence[begin_index] == item):
            return begin_index
        elif (sequence[end_index] == item):
            return end_index
        elif (midpoint_value == item):
            return midpoint
        elif (midpoint_value > item):
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

sequence_a = [1,2,3,5,8,45,67,89,123]
item_a = 3

print(binary_search(sequence_a,89))