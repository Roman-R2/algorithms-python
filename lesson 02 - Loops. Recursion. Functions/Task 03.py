"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

try:
    number = int(input("Введите первое число: "))

    str_int = str(number)

    for i in str_int:
        if int(i) % 2 == 0:
            even_digits_count += 1
        else:
            odd_digits_count += 1

    print(f"В этом числе {even_digits_count} четных цифр и {odd_digits_count} нечетных цифр.")

except ValueError:
    print("Вы ввели не натуральное число!")