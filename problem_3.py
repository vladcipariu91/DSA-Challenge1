import sys


class PriorityQueue(object):

    def __init__(self):
        self.min_heap = []

    def append(self, char_to_count):
        self.min_heap.append(char_to_count)
        heap_size = len(self.min_heap)
        if heap_size == 1:
            return
        else:
            inserted_index = heap_size - 1
            parent_index = (inserted_index - (2 - inserted_index % 2)) // 2
            while self.min_heap[parent_index][1] > self.min_heap[inserted_index][1] and inserted_index != 0:
                self.swap(parent_index, inserted_index)

                inserted_index = parent_index
                parent_index = (inserted_index - (2 - inserted_index % 2)) // 2

    def pop(self):
        if len(self.min_heap) == 0:
            return None

        result = self.min_heap[0]
        self.min_heap[0] = self.min_heap[len(self.min_heap) - 1]
        self.min_heap.pop(len(self.min_heap) - 1)

        current_index = 0
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if left_index >= len(self.min_heap) and right_index >= len(self.min_heap):
            return result

        while (left_index < len(self.min_heap) and self.min_heap[current_index][1] > self.min_heap[left_index][1]) or \
                (right_index < len(self.min_heap) and self.min_heap[current_index][1] > self.min_heap[right_index][1]):

            if self.min_heap[current_index][1] > self.min_heap[left_index][1]:
                self.swap(current_index, left_index)

                current_index = left_index
            elif self.min_heap[current_index][1] > self.min_heap[right_index][1]:
                self.swap(current_index, right_index)

                current_index = right_index
            else:
                break

            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2

            if left_index >= len(self.min_heap) or right_index >= len(self.min_heap):
                break

        return result

    def swap(self, current_index, child_index):
        temp = self.min_heap[current_index]
        self.min_heap[current_index] = self.min_heap[child_index]
        self.min_heap[child_index] = temp

    def __repr__(self):
        return str(self.min_heap)

    def __len__(self):
        return len(self.min_heap)


class HuffmanTree:

    def __init__(self, text):
        if text is None or len(text) == 0:
            self.root = None
            return

        self.__p_q = PriorityQueue()
        self.codes_map = {}
        occurrence_map = {}
        for c in text:
            if c in occurrence_map:
                occurrence_map[c] += 1
            else:
                occurrence_map[c] = 1

        for k, v in occurrence_map.items():
            self.__p_q.append((k, v))

        self.root = self.__build()
        self.__generate_codes(self.root, [], 0)

    def __build(self):
        root = None
        while self.__p_q:
            first = self.__p_q.pop()
            second = self.__p_q.pop()

            parent = Node(first[1] + second[1])

            if isinstance(first[0], Node):
                left_child = first[0]
            else:
                left_child = Node(first[0])

            if isinstance(second[0], Node):
                right_child = second[0]
            else:
                right_child = Node(second[0])

            parent.left = left_child
            parent.right = right_child

            if len(self.__p_q) != 0:
                self.__p_q.append((parent, parent.value))
            else:
                root = parent

        return root

    def get_code(self, value):
        if value in self.codes_map:
            return self.codes_map[value]
        else:
            return None

    def __generate_codes(self, node, arr, index):
        if node.left:
            if len(arr) == index:
                arr.append("0")
            else:
                arr[index] = "0"
            self.__generate_codes(node.left, arr, index + 1)

        if node.right:
            if len(arr) == index:
                arr.append("1")
            else:
                arr[index] = "1"
            self.__generate_codes(node.right, arr, index + 1)

        if node.is_leaf():
            code = ""
            for it in range(0, index):
                if it == "":
                    break
                code += arr[it]

            self.codes_map[node.value] = code


class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def is_leaf(self):
        return self.left is None and self.right is None


def huffman_encoding(data):
    tree = HuffmanTree(data)

    code = ""
    if data is not None:
        for it in data:
            part_code = tree.get_code(it)
            if part_code:
                code += part_code

    return code, tree


def huffman_decoding(data, tree):
    current = tree.root
    result = ""
    for it in data:
        if it == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            result += current.value
            current = tree.root

    return result


if __name__ == "__main__":
    def simple_test():
        a_great_sentence = "The bird is the word"

        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        # expected 36
        print("The content of the encoded data is: {}\n".format(encoded_data))
        # expected 1010111001011010111111100000110111101111100010111001011001100011100000

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        # expected 69
        print("The content of the encoded data is: {}\n".format(decoded_data))
        # expected The bird is the word


    def empty_input_test():
        empty_sentence = ""

        print("The size of the data is: {}\n".format(sys.getsizeof(empty_sentence)))
        # expected 49

        encoded_data, tree = huffman_encoding(empty_sentence)
        print("The size of the encoded data is: {}\n".format(
            0 if len(encoded_data) == 0 or encoded_data is None else sys.getsizeof(int(encoded_data, base=2))))
        # expected 0
        print("Encoded: {}".format(encoded_data))
        # expected ""

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        # expected 49
        print("Decoded: {}".format(decoded_data))
        # expected ""


    def none_input_test():
        none_sentence = None

        print("The size of the data is: {}\n".format(sys.getsizeof(none_sentence)))

        encoded_data, tree = huffman_encoding(none_sentence)
        print("The size of the encoded data is: {}\n".format(
            0 if len(encoded_data) == 0 or encoded_data is None else sys.getsizeof(int(encoded_data, base=2))))
        # expected 49
        print("Encoded: {}".format(encoded_data))
        # expected ""

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        # expected 49
        print("Decoded: {}".format(decoded_data))
        # expected ""


    def a_really_long_string():
        a_sentence = "This a test for a really long string that I just came up now. Aren't I really creative."

        print("The size of the data is: {}\n".format(sys.getsizeof(a_sentence)))

        encoded_data, tree = huffman_encoding(a_sentence)
        print("The size of the encoded data is: {}\n".format(
            0 if len(encoded_data) == 0 or encoded_data is None else sys.getsizeof(int(encoded_data, base=2))))
        # expected 76
        print("Encoded: {}".format(encoded_data))
        # expected 111101011010011110010100111110011001011010100001111110110101100101111100111001101101110100010001111111011100001011111101100110111010001001111100111110110011011001101001110000111100101011111111001100010100001101000111001001010110011110001011101111111001011101101001101111111101100110110111110110101000111100101011100110110111010001000111111101101000100110110111000111100110010010110010011

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        # expected 136
        print("Decoded: {}".format(decoded_data))
        # expected This a test for a really long string that I just came up now. Aren't I really creative.


    simple_test()
    empty_input_test()
    none_input_test()
    a_really_long_string()
