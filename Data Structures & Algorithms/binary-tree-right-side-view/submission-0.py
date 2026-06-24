# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([-1,root])
        res = []
        level = -1

        while q:
            x = q.popleft()
            if x == -1:
                if q:
                    res.append([])
                    level += 1
                    q.append(-1)
                    continue
                else:
                    break
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
            res[level].append(x.val)
        
        ret = []
        for x in res:
            ret.append(x[-1])
        return ret
        