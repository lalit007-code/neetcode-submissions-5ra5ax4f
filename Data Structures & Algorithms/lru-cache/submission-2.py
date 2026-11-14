class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0,0) , Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev,nxt
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # def remove(self)
    def get(self, key: int) -> int:
        # print(self.right.prev.val)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #if key in cache , remove it and insert new node with this value and key
        if key in self.cache:
            self.remove(self.cache[key])
        #same cache ki key ma new address
        self.cache[key] = Node(key,value)
        #self.cache krna isiliye secure hai , jisse galat address na jaye, ya tum isse kisi variable ma lekar bej skte ho
        self.insert(self.cache[key])

        #and when you inserted the value in cache ,also check , does it exceeding the cap limit

        if self.capacity < len(self.cache):
            lru = self.left.next
            print("key",lru.key,lru.val)
            self.remove(lru)
            del self.cache[lru.key]

