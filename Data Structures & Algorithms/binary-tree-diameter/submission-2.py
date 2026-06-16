# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0]

        def find_height(root):
            if not root:
                return 0
            
            left = find_height(root.left)
            right = find_height(root.right)
            diam = left + right

            max_d[0] = max(max_d[0], diam)

            return 1 + max(left, right)

        find_height(root)

        return max_d[0]
        


        

        

        