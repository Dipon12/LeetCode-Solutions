class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        temp = head
        while temp!=None:
            temp = temp.next
            count += 1
        no = count - n
        count = 1
        temp = head
        
        if no == 0:
            head = head.next
            return head
        
        while temp!=None:
            if count == no:
                temp.next = temp.next.next
                return head
            
            temp = temp.next
            count+=1
                
            