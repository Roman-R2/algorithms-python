"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
import random
from statistics import median

if __name__ == '__main__':
    # Сгенерируем список с нечетным колличеством элементов, лучше бы кортеж, но ксловия задачим такие
    emulate_list = [random.randrange(0, 10) for _ in range(1, 10)]
    print(f"Исходный список: {emulate_list}")
    print(f"Для проверки: {median(emulate_list)}")

    # Скопируем в список, чтобы не изменить исходный
    list_for_search = emulate_list.copy()

    left_part = []
    middle = len(list_for_search) // 2 + 1
    for i in range(middle):
        get_min = list_for_search.pop(list_for_search.index(min(list_for_search)))
        if i == middle - 1:
            print(f"Медиана: {get_min}. Левая упорядоченная часть {left_part}")
            break
        left_part += [get_min]
