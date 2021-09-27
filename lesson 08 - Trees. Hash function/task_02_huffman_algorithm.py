"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter


# В данном случае узел - это элемент, у которого всегля есть левый и правий узел или лист
class HuffmanNode:
    def __init__(self, left, right, frequency):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.data = 'not_leaf'


class HuffmanAlgorithm:
    def __init__(self, string):
        if len(string) < 3:
            self.error(f"Нет смысла использовать алгоритм Хаффмана с длиной строки {len(string)}")
        else:
            self.string = string
            self.get_code_table()
            self.code_dict = {}

    def error(self, message) -> None:
        print(f"------------------------\n{self.__class__} : {message}\n------------------------\n")

    def get_string_frequency(self) -> dict:
        char_frequency = dict(Counter(self.string))
        char_frequency = self.sort_frequency_dict(char_frequency)
        return char_frequency

    def sort_frequency_dict(self, frequency):
        """
        Функция сортирует словарь по значению в порядке убывания
        :param frequency: словарь для сортировки
        :return: отсортированный по убыванию словарь
        """
        return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

    def create_bst(self):
        frequency = self.get_string_frequency()
        print(frequency)
        # Если строка состояла только из одного символа
        if len(frequency) < 2:
            self.error(f"С отдим символьм дерево не построить.")
            return None
        huffman_node = None
        while len(frequency) > 1:
            last_1 = frequency.popitem()
            last_2 = frequency.popitem()
            huffman_node = HuffmanNode(last_2, last_1, (last_1[1] + last_2[1]))
            frequency.update({huffman_node: (last_2[1] + last_1[1])})
            frequency = self.sort_frequency_dict(frequency)
        return huffman_node

    def get_code_table(self):
        huffman_bsd = self.create_bst()
        print(huffman_bsd.left[0])
        if not huffman_bsd:
            return None
        else:
            code_table = self._get_code_table(huffman_bsd, "0", "1")
        print(code_table)
        return code_table

    def _get_code_table(self, huffman_bsd, l_code: str, r_code: str):
        if isinstance(huffman_bsd.left[0], HuffmanNode):
            self._get_code_table(huffman_bsd.left[0], l_code+"0", r_code+"0")
        else:
            self.code_dict.update({huffman_bsd.left[0]: l_code})
        if isinstance(huffman_bsd.right[0], HuffmanNode):
            self._get_code_table(huffman_bsd.right[0], f"{l_code}1", f"{r_code}1")
        else:
            self.code_dict.update({huffman_bsd.left[0]: r_code})
        return self.code_dict


if __name__ == '__main__':
    message = "beep boop beer!"

    huffman = HuffmanAlgorithm(message)

    print(huffman)
