# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

            curr = root

            while curr:
                # if (p.val < curr.val and q.val > curr.val) or (p.val > curr.val and q.val < curr.val):
                #     return curr
                
                # if p.val == curr.val or q.val == curr.val:
                #     return curr
                
                if p.val > curr.val and q.val > curr.val:
                    curr = curr.right
                elif p.val < curr.val and q.val < curr.val:
                    curr  = curr.left
                else:
                    return curr
                        
        
        # p_anc = []
        # q_anc = []

        # def dfs(root):
        #     if not root:
        #         return None
            
        #     if root.left and root.left.val == p.val:
        #         p_anc.append(p.val)
        #         p_anc.append(root.left.val)
            
        #     if root.right and root.right.val == p.val:
        #         p_anc.append(p.val)
        #         p_anc.append(root.right.val)
            
        #     if root.left and root.left.val == q.val:
        #         q_anc.append(q.val)
        #         q_anc.append(root.left.val)
            
        #     if root.right and root.right.val == q.val:
        #         q_anc.append(q.val)
        #         q_anc.append(root.right.val)
                
        #     if len(p_anc) == 2 and len(q_anc) == 2:
        #         return list(set(p_anc) & set(q_anc))

        #     dfs(root.left)
        #     dfs(root.right)
        
        # ans = dfs(root)
        # print(ans)
        # return ans[0]
