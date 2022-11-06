# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None or head.next.next == None : return head
        
        odd, even, even_start = head, head.next, head.next
        odd.next = odd.next.next
        odd = odd.next
        
        prev = None
        
        while(odd):
            if odd.next != None :
                even.next = odd.next
                even = even.next
                
                odd.next = odd.next.next
                prev = odd
                odd = odd.next
                
                if odd == None :
                    even.next = None
                    prev.next = even_start
                    break
                
            else :
                even.next = None
                odd.next = even_start
                break
        
        return head
            
