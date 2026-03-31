# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        stk = []
        curr = head
        while curr:
            stk.append(curr)
            curr = curr.next
        
        head = stk[-1]
        while stk:
            popped = stk.pop()
            if stk:
                popped.next = stk[-1]
            else:
                popped.next = None
            

        return head
            
