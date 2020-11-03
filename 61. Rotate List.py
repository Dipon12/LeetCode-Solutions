# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        count=0
        
        temp = head
        while temp!=None:
            count+=1
            tail = temp
            temp = temp.next
        
        if count==0 or k%count==0:
            return head
        
        count = count - k%count

        
        temp = head
        
        c=0
        
        while temp!=None:
            if c==count-1:
                new_head = temp.next
                tail.next = head
                temp.next = None
                break
            
            temp = temp.next
            c+=1
            
        return new_head
        
        
            