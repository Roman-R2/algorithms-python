"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict


def get_input_for_hex(number_of_input: int):
    """
    Функция берет строку с ввода, проверяет, что это шестнадцатиричное число и создает словарь, где ключем
    является число в десятичной системе, а значением список символов ввода шестнадцатиричной системе,
    для каждого введеноего шестнадцатиричного числа
    :param number_of_input: сколько хотим ввести шестнадцатиричных чисел
    :return: словарь где ключем  является число в десятичной системе, а значением список символов ввода в
    шестнадцатиричной системе
    """
    input_dict = defaultdict(list)
    for i in range(1, number_of_input + 1):
        while True:
            try:
                hex_first_number = str(input(f"Введите {i} число в шестнадцатиричной системе: "))
                dec_first_number = int(hex_first_number, 16)
                for char in hex_first_number:
                    input_dict[dec_first_number].append(char)
                break
            except ValueError:
                print("Вы должны ввести число в шестнадцатеричной системе счисления!")
    return input_dict


if __name__ == '__main__':
    print("Введите два числа в шестнадцатеричной системе счисления.")
    two_hex_input_dict = get_input_for_hex(2)
    print(two_hex_input_dict)

    dec_sum_of_two_number = 0
    dec_multiplication_of_two_number = 1
    for dec, hex_list in two_hex_input_dict.items():
        dec_sum_of_two_number += dec
        dec_multiplication_of_two_number *= dec

    hex_sum_of_two_number = format(dec_sum_of_two_number, 'X')
    hex_multiplication_of_two_number = format(dec_multiplication_of_two_number, 'X')

    print(f"Сумма чисел: {list(hex_sum_of_two_number)}")
    print(f"Произведение чисел: {list(hex_multiplication_of_two_number)}")

    # Можно было и проще
    print("---> Второй вариант решения: ")
    first = 'a2'
    second = 'c4f'
    print(f"Сумма: {list(format(int(first, 16) + int(second, 16), 'X'))}")
    print(f"Произведение: {list(format(int(first, 16) * int(second, 16), 'X'))}")
