# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            q = deque([root])
        else:
            return 0
        
        res = 1

        q.append(-200)

        while q:
            top = q.popleft()
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
            if q[0] == -200:
                q.popleft()
                if q:
                    q.append(-200)
                res += 1
        
        return res-1
            
'''
[4,-200]

'''
