class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.insert(key, value)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node) -> None:
        prev = node.prev
        nxt  = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node) -> None:
        prev = self.right.prev
        nxt  = self.right
        prev.next = node
        nxt.prev



# Get
# 1. remove: prev -> now -> next
# 2. insert: prev -> next -> new

# Put
# 1. remove: prev -> now -> next
# 2. insert: prev -> next -> new

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)

actions = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
key_value = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

for i in range(len(actions)):
    action = actions[i]
    if action == "put":
        key, value = key_value[i]
        obj.put(key,value)
    else:
        key = key_value[i]
        param_1 = obj.get(key)
        print(param_1)
