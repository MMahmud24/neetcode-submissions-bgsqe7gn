# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        
        ''' 
        res = [[1], [2,3], []]
        q = [-1,]
        x = -1
        level = 1
        '''
    
        return res


                
            
            
