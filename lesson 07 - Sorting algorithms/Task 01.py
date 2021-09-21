"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random


def swap(some_list: list, left_index: int, right_index: int) -> None:
    """
    Функция переставит элементы списка местами, если они не равны
    :param some_list: список для перестановки
    :param left_index: левый индекс для перестановки
    :param right_index: правый индекс для перестановки
    :return: None
    """
    # Это условие обеспечивает устойчивость алгоритма (порядок одинаковых элементов в списке будет сохранен)
    if some_list[left_index] != some_list[right_index]:
        some_list[left_index], some_list[right_index] = some_list[right_index], some_list[left_index]


# Эта функция для упрощения восприятия кода
def get_expression(reverse: bool, left_part, right_part) -> bool:
    if reverse:
        expression = left_part < right_part
    else:
        expression = left_part > right_part
    return expression


# Алгоритм доработан таким образом, что если во время выполнения цикла for
# не было перстановок (is_swapped = False), то мы завершаем циклы
def bubble_sort(some_list: list, reverse: bool = False) -> list:
    """
    Функция сортирует список метолом пузырька
    :param some_list: список для сортировки
    :param reverse: False сортирует по возрастанию, True по убыванию
    :return: вернет отсортированный список
    """
    n: int = 1

    while n < len(some_list):
        is_swapped: bool = False
        for i in range(len(some_list) - n):
            if get_expression(reverse, some_list[i], some_list[i + 1]):
                swap(some_list, i, i + 1)
                is_swapped = True
            # Если мы дошли до конца
            if i == len(some_list) - n:
                if not is_swapped:
                    break
                is_swapped = False
        if not is_swapped:
            print(f"Потребовалось {n} проходов по while")
            break
        n += 1
    else:
        # Это если пришлось использовать максимальное колличество проходов
        # (is_swapped = False когда n < len(some_list))
        print(f"Потребовалось {n} проходов по while")
    return some_list


if __name__ == '__main__':
    emulate_list = [random.randrange(-101, 100) for _ in range(1, 20)]

    print(f"Исходный список: {emulate_list}")

    bubble_sort(emulate_list, True)
    print(f"Отсортированный список: {emulate_list}")
