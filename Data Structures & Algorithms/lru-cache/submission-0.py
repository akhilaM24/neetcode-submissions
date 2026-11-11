class Node:
    # Script: each node stores one key-value pair and links to neighbors
    # in the recency list. Keeping the key on the node lets us remove it
    # from the hash map when it is evicted from the list.
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # Script: store the maximum number of entries allowed.
        self.capacity = capacity
        # Script: hash map from key to its node for O(1) lookup.
        self.cache = {}
        # Script: sentinel head and tail so every real node always has
        # a prev and next, removing the need for edge-case checks.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        # Script: unlink a node from wherever it sits in the list.
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: Node) -> None:
        # Script: insert the node right after head, marking it most recent.
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        # Script: if the key is absent, the answer is -1 with no reordering.
        if key not in self.cache:
            return -1
        # Script: the key was used, so move its node to the most recent end.
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # Script: if the key already exists, update it and mark it recent.
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return
        # Script: a new key. If we're at capacity, evict the least recent
        # node, which sits just before the tail sentinel.
        if len(self.cache) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        # Script: create the new node, register it in the map, and place it
        # at the most recent position.
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)