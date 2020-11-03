# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        str1 = ""
        str2 = ""
        
        while l1!=None:
            str1 = str1+str(l1.val)
            l1=l1.next
            
        while l2!=None:
            str2 = str2+str(l2.val)
            l2=l2.next
        
        str1 = int(str1)
        str2 = int(str2)
        
        ans = str1 + str2
        
        ans = str(ans)
        
        head = ListNode(str(ans[0]))
        l = len(ans)
        prev_temp = head
        for i in range(1,l):
            temp = ListNode(ans[i])
            prev_temp.next = temp
            prev_temp = temp
            
        prev_temp.next = None
         
        return head