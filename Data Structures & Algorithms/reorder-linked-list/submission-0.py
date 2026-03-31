# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stk = []

        curr = head
        while curr:
            stk.append(curr)
            curr = curr.next

        
        curr = head
        for i in range(len(stk) // 2):
            temp = curr.next
            node = stk.pop() 
            curr.next = node 
            node.next = temp 
            curr = temp 

        curr.next = None

        