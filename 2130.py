# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middle_(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
    def reverse_(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        mid  = self.middle_(head) 
        prev = self.reverse_(mid)
        curr = head
        
        MAX = 0
        while(prev):
            MAX = max(MAX, prev.val + curr.val)
            prev = prev.next
            curr = curr.next        
        
        return MAX
        
        
        
