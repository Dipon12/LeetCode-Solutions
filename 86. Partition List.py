# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        flag1 = 0
        flag2 = 0
        if head == None:
            return head
        
        head1 = head2 = None
        
        
        while head!= None:
            if head.val<x:
                flag1 = 1
                if head1 == None:
                    head1 = head
                    temp1 = head1
                else:
                    temp1.next = head
                    temp1 = temp1.next
            else:
                flag2 = 1
                if head2 == None:
                    head2 = head
                    temp2 = head2
                else:
                    temp2.next = head
                    temp2 = temp2.next
                    
            head = head.next
        
        if flag1 == 1 and flag2 ==1:
            temp1.next = head2
            temp2.next = None
            return head1
        elif flag1 == 0:
            temp2.next = None
            return head2
        else:
            temp1.next = None
            return head1
        