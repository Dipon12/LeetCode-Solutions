# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        count = 1 
        
        if head!= None and head.next!= None:
            t1 = head
            t2 = head.next
            t1.next = t2.next
            t2.next = t1
            head = t2
            temp = t1
            pre_temp = t1
        else:
            return head
        
        temp = temp.next
        
        while temp!=None:
            t1 = temp
            t2 = temp.next
            if t2==None:
                t1.next = None
                pre_temp.next = t1 
            else:
                t1.next = t2.next
                t2.next = t1
                pre_temp.next = t2
            pre_temp = temp
            temp = temp.next
        return head
            