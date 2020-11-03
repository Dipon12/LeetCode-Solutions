# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        stack = []
        pos = []
        count = i = 0
        res = []
        
        while head!=None:
            res.append(0)
            
            if len(stack)==0:
                stack.append(head.val)
                pos.append(i)
            else:
                if head.val<stack[len(stack)-1]:
                    stack.append(head.val)
                    pos.append(i)
                else:
                    while len(stack)!=0 and stack[len(stack)-1]<head.val:
                        res[pos[len(stack)-1]] = head.val
                        stack.pop()
                        pos.pop()
                    stack.append(head.val)
                    pos.append(i)
            head = head.next
            i+=1
            
        
        return res