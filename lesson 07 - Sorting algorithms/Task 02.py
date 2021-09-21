"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import numpy as np


# np.random.uniform(a, b) # range [a, b)

def merge_two_lists(list_one: list, list_two: list):
    pointer_one = pointer_two = 0
    len_one = len(list_one)
    len_two = len(list_two)
    merged_list = []
    while pointer_one < len_one and pointer_two < len_two:
        if list_one[pointer_one] < list_two[pointer_two]:
            merged_list.append(list_one[pointer_one])
            pointer_one += 1
        else:
            merged_list.append(list_two[pointer_two])
            pointer_two += 1
    while pointer_one < len_one:
        merged_list.append(list_one[pointer_one])
        pointer_one += 1
    while pointer_two < len_two:
        merged_list.append(list_two[pointer_two])
        pointer_two += 1
    return merged_list


def merge_sort(unsorted_list: list) -> list:
    if len(unsorted_list) == 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left = merge_sort(unsorted_list[:middle])
    right = merge_sort(unsorted_list[middle:])
    return merge_two_lists(left, right)


if __name__ == '__main__':
    emulate_list = [np.round(np.random.uniform(0, 50), 2) for _ in range(1, 20)]

    print(f"Исходный список: {emulate_list}")
    print(type(emulate_list[0]))
    print(f"Отсортированный список: {merge_sort(emulate_list)}")
