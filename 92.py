# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right : return head
        
        if left == 1 :
            idx = 0
            front = head
            prev = None
            curr = head
            while(idx < right):
                idx += 1
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            front.next = temp
            return prev
                
            
        else :
            
            idx = 1
            curr = head
            front = None
            while(idx < left):
                idx += 1
                front = curr
                curr = curr.next
                
            
            prev = None
            while(idx <= right):
                idx += 1
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            last = front.next
            front.next = prev
            last.next = temp
            
                
            return head
        
        
        
        
