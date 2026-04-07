"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    # def __init__(self):
        # not needed 
        # self.left = Node(0)
        # self.right = Node(0)
        # self.left.next = self.right
        # self.right.prev = self.left

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        # not neeeded
        # i = 0
        # cll = self.left
        oldToCopy = {None:None} # val : index
        while cur:
            # not needed
            # node,prev,nxt = Node(cur.val),cll,cll.next
            # prev.next = nxt.prev = node
            # node.prev = prev
            # node.next = nxt
            # return self.left.next
            #updating the pointer
            # cll = node
            
            #new node using Node
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
            
        return oldToCopy[head]





        
        