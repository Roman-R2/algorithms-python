"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def get_count_various_substring(string, verbose=False):
    various_hash = []

    iteartion_count = 0
    for count in range(0, len(string)):
        for pos in range(len(string) - count):
            # Прочситаем количество итераций циклов
            iteartion_count += 1
            substring = string[pos:(pos + count + 1)]
            hash_substring = hashlib.sha1(substring.encode('utf-8')).hexdigest()

            # Подстрока это строка, то пропускаем
            if pos == 0 and pos + count + 1 == len(string):
                continue

            if hash_substring not in various_hash:
                various_hash.append(hash_substring)

            if verbose:
                print(iteartion_count, f"[{pos}:{(pos + count + 1)}]", substring, hash_substring)

    return len(various_hash)


if __name__ == '__main__':
    string = "Fear is the mind-killer"
    print("Различных подстрок: ", get_count_various_substring(string, True))
