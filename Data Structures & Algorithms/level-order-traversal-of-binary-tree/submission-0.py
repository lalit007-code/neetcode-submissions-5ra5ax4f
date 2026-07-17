# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([root])
        ans = []

        while dq:
            lengthDq = len(dq)
            level = []
            print(lengthDq)
            for i in range(lengthDq):
                node = dq.popleft()
                if node:
                    level.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
            if level:
                ans.append(level)
        return ans