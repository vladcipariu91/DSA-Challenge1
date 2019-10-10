class LRUCache(object):

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__doublyLinkedList = DoublyLinkedList()
        self.__node_map = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        found_node = self.__find_node(key)
        if found_node is None:
            return -1

        self.__set_most_recently_used(found_node)
        return found_node.value

    def set(self, key, value):
        if self.__doublyLinkedList.count >= self.__capacity:
            removed_node = self.__doublyLinkedList.tail
            self.__doublyLinkedList.remove_last()
            if removed_node is not None:
                self.__node_map.pop(removed_node.key)

        self.__doublyLinkedList.add_first(key, value)
        added_node = self.__doublyLinkedList.head
        self.__node_map[added_node.key] = added_node

    def __find_node(self, key):
        return self.__node_map.get(key)

    def __set_most_recently_used(self, current_node):
        if current_node == self.__doublyLinkedList.head:
            return

        next_node = None
        if current_node == self.__doublyLinkedList.tail:
            self.__doublyLinkedList.tail = current_node.previous
        else:
            next_node = current_node.next
            next_node.previous = current_node.previous

        current_node.previous.next = next_node

        current_node.previous = None
        current_node.next = self.__doublyLinkedList.head
        self.__doublyLinkedList.head.previous = current_node
        self.__doublyLinkedList.head = current_node

    # test helper function
    def to_list(self):
        return self.__doublyLinkedList.to_list()

    # test helper function
    def map_size(self):
        return len(self.__node_map)


class Node(object):

    def __init__(self, key, value):
        self.previous = None
        self.next = None
        self.key = key
        self.value = value

    def __repr__(self):
        return "Node( key: {}, value: {} ) ".format(self.key, self.value)


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_first(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = self.head.previous

        self.count += 1

    def remove_last(self):
        if self.head is None:
            return

        self.tail.previous.next = None
        self.tail = self.tail.previous
        self.tail.next = None

        self.count -= 1

    def size(self):
        return self.count

    def to_list(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.value)
            current = current.next

        return result

    def __repr__(self):
        current = self.head
        print_result = ""
        while current is not None:
            print_result += str(current)
            current = current.next

        return print_result


# Testing

def test_cache_hit_first():
    lru_cache = LRUCache(5)

    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)

    print(lru_cache.get(3))
    # expected 3
    print(lru_cache.to_list())
    # expected [3, 2, 1]


def test_cache_hit_middle():
    lru_cache = LRUCache(5)

    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)

    print(lru_cache.get(2))
    # expected 2
    print(lru_cache.to_list())
    # expected [2, 3, 1]


def test_cache_hit_last():
    lru_cache = LRUCache(5)

    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)

    print(lru_cache.get(1))
    # expected 1
    print(lru_cache.to_list())
    # expected [1, 3, 2]
    print(lru_cache.map_size())
    # expected 3


def test_cache_miss():
    lru_cache = LRUCache(5)

    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)

    print(lru_cache.get(4))
    # expected -1
    print(lru_cache.to_list())
    # expected [3, 2, 1]
    print(lru_cache.map_size())
    # expected 3


def test_set_when_cache_is_full():
    lru_cache = LRUCache(5)

    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)
    lru_cache.set(4, 4)
    lru_cache.set(5, 5)

    print(lru_cache.to_list())
    # expected [5, 4, 3, 2, 1]
    print(lru_cache.map_size())
    # expected 5

    lru_cache.set(6, 6)

    print(lru_cache.to_list())
    # expected [6, 5, 4, 3, 2]
    print(lru_cache.map_size())
    # expected 5


def test_empty():
    lru_cache = LRUCache(5)

    print(lru_cache.get(4))
    # expected -1
    print(lru_cache.map_size())
    # expected 0
    print(lru_cache.to_list())
    # expected []


test_cache_hit_first()
test_cache_hit_middle()
test_cache_hit_last()
test_cache_miss()
test_set_when_cache_is_full()
test_empty()
