# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [1]
        value = [0]

        def in_order(root):
            if not root:
                return None
            
            in_order(root.left)
            if count[0] == k:
                value[0] = root.val
            count[0] += 1
            in_order(root.right)

        in_order(root)

        return(value[0])
