# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        temp = head
        
        dic = {}
        
        while temp!=None:
            v = dic.get(id(temp),-1)
            
            if v==-1:
                dic[id(temp)] = 1      
            else:
                return True
                
            temp = temp.next
        return False
            