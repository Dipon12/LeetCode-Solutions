# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 1 
        ans = head
        while head!=None:
            if count%2 == 0:
                ans = ans.next
            
            count+=1
            head=head.next
            
        return ans