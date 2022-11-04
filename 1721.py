# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        LEN = 0
        curr = head
        while(curr):
            LEN += 1
            curr = curr.next
            
        loc0 = min(k, LEN - k + 1)
        loc1 = max(k, LEN - k + 1)
            
        idx = 1
        curr = head
        while(idx <= loc1):
            
            if idx == loc0 : A = curr.val
            if idx == loc1 : B = curr.val
            
            idx += 1
            curr = curr.next
            
        idx = 1
        curr = head
        while(idx <= loc1):
            
            if idx == loc0 : curr.val = B
            if idx == loc1 : curr.val = A
            
            idx += 1
            curr = curr.next
            
        return head
        
