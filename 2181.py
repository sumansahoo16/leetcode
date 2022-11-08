# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def add_ans_node(ans, temp):
    if ans.val == -1:
        ans.val = temp
        return 
    node = ListNode(val = temp)
    ans.next = node
    ans = ans.next 
    
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        start = ListNode(val = -1)
        ans = start
        
        curr = head.next
        temp = 0
        while(curr):
            
            if curr.val == 0 :
                if ans.val == -1:
                    ans.val = temp
                     
                else :
                    node = ListNode(val = temp)
                    ans.next = node
                    ans = ans.next 
                    
                temp = 0
            else : temp += curr.val
                
            curr = curr.next
        
        return start
        
