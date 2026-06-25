# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []

        def in_order(root):
            if not root:
                return None
            
            in_order(root.left)
            res.append(root.val)
            in_order(root.right)
            
        in_order(root)

        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False

        return True

        