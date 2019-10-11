"""
You will take in two linked lists and return a linked list that is composed of either the union or intersection,
respectively.
Once you have completed the problem you will create your own test cases and
perform your own run time analysis on the code.
"""


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = TreeNode(value)

    def get_root(self):
        return self.root

    def to_linked_list(self):
        result = LinkedList()
        self.in_order(self.root, result)
        return result

    def in_order(self, node, linked_list):
        if node:
            self.in_order(node.left, linked_list)
            linked_list.append(node.value)
            self.in_order(node.right, linked_list)

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        self.__insert_with_recursion(self.root, new_node)

    def __insert_with_recursion(self, node, new_node):
        if self.compare(node, new_node) == -1:
            if node.left is None:
                node.left = new_node
            else:
                self.__insert_with_recursion(node.left, new_node)
        elif self.compare(node, new_node) == 1:
            if node.right is None:
                node.right = new_node
            else:
                self.__insert_with_recursion(node.right, new_node)
        else:
            return

    def search(self, value):
        return self.search_rec(self.root, value)

    def search_rec(self, node, value):
        if node:
            if node.value == value:
                return True

            if value < node.value:
                return self.search_rec(node.left, value)
            elif value > node.value:
                return self.search_rec(node.right, value)
        else:
            return False


class TreeNode(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    if llist_1 is None:
        return llist_2
    if llist_2 is None:
        return llist_1
    # Your Solution Here
    tree = Tree()

    current_1 = llist_1.head
    current_2 = llist_2.head

    while current_1 or current_2:
        if current_1:
            tree.insert(current_1.value)
            current_1 = current_1.next
        if current_2:
            tree.insert(current_2.value)
            current_2 = current_2.next

    return tree.to_linked_list()


def intersection(llist_1, llist_2):
    if llist_1 is None or llist_2 is None:
        return None

    # Your Solution Here
    l1_size = llist_1.size()  # O(n)
    l2_size = llist_2.size()  # O(n)

    if l1_size >= l2_size:
        return do_intersection(llist_2.head, build_tree(llist_1))
    else:
        return do_intersection(llist_1.head, build_tree(llist_2))


def do_intersection(head, tree):
    current = head
    result = Tree()
    while current:
        if tree.search(current.value):
            result.insert(current.value)

        current = current.next

    return result.to_linked_list()


def build_tree(llist):
    current = llist.head
    tree = Tree()
    while current:
        tree.insert(current.value)
        current = current.next

    return tree

if __name__ == '__main__':
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    # expected 1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 ->
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    # expected 4 -> 6 -> 21 ->

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    # 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65 ->
    print(intersection(linked_list_3, linked_list_4))
    # expected ""

    # Test case 3
    linked_list_5 = None
    linked_list_6 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    for i in element_1:
        linked_list_6.append(i)

    print(union(linked_list_5, linked_list_6))
    # expected 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 ->
    print(intersection(linked_list_3, linked_list_4))
    # expected ""
