"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы
с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной
и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""

# Python 3.8.8
# Тип системы:  x64-based PC

# https://pympler.readthedocs.io/en/latest/
from pympler import asizeof
import random


def format_the_output(func):
    def inner(*args, **kwargs):
        print("-------- Начало --------->")
        print("Оценка памяти для задания: ")
        result = func(*args, **kwargs)
        print("-------- Конец --------->")
        return result

    return inner


@format_the_output
def examine_memory(verbose, *args):
    total = 0
    for item in args:
        total += asizeof.asizeof(item)
    print(f"Для задания потребовалось {total} байт")
    print("Более детально: ")
    for item in args:
        print(asizeof.asized(item, detail=verbose).format())
    return 1


#########
# 1. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#########
# Решение:

emulate_list = [random.randrange(-100, 100) for x in range(1, 40)]
negative_elements = [x for x in emulate_list if x < 0]
print(f"Максимальный отрицательный элемент: {max(negative_elements)}")

# Оценка памяти:
examine_memory(0, emulate_list, negative_elements, max(negative_elements))
# Оценка памяти для задания:
# Для задания потребовалось 2256 байт
# Более детально:
# [71, -17, 34, 54, -46, 39, 66, 50, 16,...., 64, 92, 70, 11, 48, -86, 19, 81, 28] size=1624 flat=376
# [-17, -46, -95, -13, -25, -77, -22, -34, -50, -76, -21, -75, -86] size=600 flat=184
# -13 size=32 flat=32
# -------- Конец --------->


#########
# 2. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
#########
# Решение:
digit_frequency = 0
state_1 = digit_frequency
emulate_sequence_of_numbers = []
state_2 = emulate_sequence_of_numbers
for i in range(10):
    emulate_sequence_of_numbers += [random.randint(100, 1000000)]
state_3 = emulate_sequence_of_numbers
print("Введенная последовательность чисел: ", emulate_sequence_of_numbers)

while True:
    try:
        # Тут должен быть inpyt(), но его нет :)
        search_digit = 7
        state_4 = search_digit
        if search_digit < 0 or search_digit > 9:
            raise ValueError()
        break
    except ValueError:
        print("Вы ввели не натуральное число!")

search_digit = str(search_digit)
state_5 = search_digit

state_6 = []
state_7 = []
for number in emulate_sequence_of_numbers:
    state_6 += [number]
    for digit in str(number):
        state_7 += [digit]
        if digit == search_digit:
            digit_frequency += 1

state_8 = digit_frequency
print(f"--> Цифра {search_digit} встречалась {digit_frequency} раз")

# Оценка памяти:
examine_memory(0, state_1, state_2, state_3, state_4, state_5, state_6, state_7, state_8)


# -------- Начало --------->
# Оценка памяти для задания:
# Для задания потребовалось 2784 байт
# Более детально:
# 0 size=24 flat=24
# [112362, 89519, 461099, 572526, 912149, 906744, 206499, 738358, 387373, 203979] size=504 flat=184
# [112362, 89519, 461099, 572526, 912149, 906744, 206499, 738358, 387373, 203979] size=504 flat=184
# 7 size=32 flat=32
# '7' size=56 flat=56
# [112362, 89519, 461099, 572526, 912149, 906744, 206499, 738358, 387373, 203979] size=504 flat=184
# ['1', '1', '2', '3', '6', '2', '8', '9....7', '3', '2', '0', '3', '9', '7', '9'] size=1128 flat=568
# 6 size=32 flat=32
# -------- Конец --------->

#########
# 3. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
#########
# Решение:
def pop_min_element(target_list: list) -> int:
    """
    Функция возвращает первый встреченный минимальный жлемент из списка, удаляя данный элемент из списка
    :param target_list:
    :return:
    """
    global state_1

    min_value = target_list.pop(target_list.index(min(target_list)))
    state_1 = min_value
    return min_value


emulate_list = [random.randrange(1, 100) for x in range(1, 20)]
state_2 = emulate_list

first_min_value = pop_min_element(emulate_list)
state_3 = first_min_value
second_min_value = pop_min_element(emulate_list)
state_4 = second_min_value

print(f"Первый минимальный элемент: {first_min_value}\nВторой минимальный элемент: {second_min_value}")

# Оценка памяти:
examine_memory(0, state_1, state_2, state_3, state_4)
# -------- Начало --------->
# Оценка памяти для задания:
# Для задания потребовалось 856 байт
# Более детально:
# 8 size=32 flat=32
# [80, 92, 35, 15, 83, 46, 11, 71, 53, 65, 95, 64, 19, 59, 83, 28, 31] size=760 flat=248
# 5 size=32 flat=32
# 8 size=32 flat=32
# -------- Конец --------->
