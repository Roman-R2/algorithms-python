"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter


class HuffmanNode:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


# Создать дерево Хаффмана
class HuffmanTree(object):
    # По идее дерева Хаффмана: на основе узла построить дерево Хаффмана в обратном порядке
    def __init__(self, message_for_code):
        self.code_dict = {}
        self.code_string = ""
        self.message_for_code = message_for_code
        self.frequency_dict = self.get_string_frequency(message_for_code)
        self.Leaf = [HuffmanNode(k, v) for k, v in self.frequency_dict.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node: node.value, reverse=True)
            n = HuffmanNode(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def hu_generate(self, huffman_tree, length):
        node = huffman_tree
        if not node:
            return
        elif node.name:
            t_code = ''
            for i in range(length):
                t_code += f"{self.Buffer[i]}"
            self.code_dict.update({node.name: t_code})
            return
        self.Buffer[length] = 0
        self.hu_generate(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.hu_generate(node.rchild, length + 1)

    def get_code(self):
        self.hu_generate(self.root, 0)
        self._coding()
        self.show_coding_details()

    def _coding(self):
        for char in self.message_for_code:
            self.code_string += self.code_dict.get(char)

    def show_coding_details(self):
        print(f"Исходная строка: {self.message_for_code}")
        print(f"Частота вхождения символов в строку: {self.frequency_dict}")
        print(f"Словарь кодирования: {self.code_dict}")
        print(f"Закодированная строка: {self.code_string}")

    def get_string_frequency(self, string) -> dict:
        char_frequency = dict(Counter(string))
        return char_frequency

    def sort_frequency_dict(self, frequency):
        """
        Функция сортирует словарь по значению в порядке убывания
        :param frequency: словарь для сортировки
        :return: отсортированный по убыванию словарь
        """
        return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))


if __name__ == '__main__':
    message = "beep boop beer!"

    h_tree = HuffmanTree(message)
    h_tree.get_code()
