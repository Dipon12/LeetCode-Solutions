# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dic = {}
        pre_temp = None
        temp = head
        while temp!=None:
            v = dic.get(temp.val,None)
            if v==None:
                dic[temp.val] = 1
                pre_temp = temp
            else:
                pre_temp.next=temp.next
            
            
            temp = temp.next
            
        return head