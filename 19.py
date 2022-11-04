# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        curr = head
        idx = 0
        while(curr):
            curr = curr.next
            if idx > n : prev = prev.next
            idx += 1
            
        if idx == n : return head.next
        
        if prev.next : prev.next = prev.next.next
        else : prev.next = None
        

        return head
        
        
