class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def _remove_node(self, node):
        if node is self.head or node is self.tail:
            raise Exception("Cannot remove head or tail nodes.")
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_end(self, node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_end(node)
            return node.value
        return None

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_end(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                self._remove_node(lru_node)
                del self.cache[lru_node.key]


def fibonacci(n, cache):
    if n in cache.cache:
        return cache.get(n)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        cache.put(n, result)
        return result

if __name__ == "__main__":
    cache = LRUCache()
    n = 500
    print(fibonacci(n, cache))
