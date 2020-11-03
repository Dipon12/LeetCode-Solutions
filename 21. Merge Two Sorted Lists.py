class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1!=None and l2!=None:
            if l1.val<l2.val:
                head = l1
                temp = l1
                temp1 = l1.next
                temp2 = l2
            else:
                head = l2
                temp =l2
                temp2 = l2.next
                temp1 = l1
                
        elif l1!=None:
            head = l1
            temp = l1
            temp1 = l1.next
            temp2 = l2
        elif l2!=None:
            head = l2
            temp =l2
            temp2 = l2.next
            temp1 = l1
        else:
            return l1
        
        while True:
            if temp1 == None:
                temp.next = temp2
                temp = temp.next
                return head
            elif temp2 == None:
                temp.next = temp1
                temp = temp.next
                return head     
            
            if temp1.val<temp2.val:
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp=temp.next
                temp2 = temp2.next
                
            
            