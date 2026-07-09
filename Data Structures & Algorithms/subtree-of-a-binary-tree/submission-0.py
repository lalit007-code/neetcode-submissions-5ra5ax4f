# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        if not t:
            return True
        
        if not s:
            return False
        
        if self.sameTree(s,t):
            return True
        
        return (self.isSubtree(s.left,t) or self.isSubtree(s.right,t))
         
        

    def sameTree(self,s,t) -> bool:
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return (self.sameTree(s.left,t.left) and self.sameTree(s.right,t.right))

        # check lagaya hai upar but we are not using it, like it should be , becuase below code of line should 
        # under above if condition        
        # if (self.sameTree(s.left,t.left) and self.sameTree(s.right,t.right)):
        #     return True

        return False
        # if subRoot == None or root == None:
        #     return False
        
        # if subRoot.val == root.val:
        #     return True


        # if self.isSubTree(root.left,subRoot.right):
        #     sr = subRoot
        # else:
        #     self.isS


        # def dfs(r,sr):
