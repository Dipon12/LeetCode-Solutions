# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        count = ans = 0
        temp=head
        while temp!=None:
            count+=1
            temp = temp.next
        
        count-=1
        while head!=None:
            ans += head.val * 2**count
            count-=1
            head = head.next
        return ans
        