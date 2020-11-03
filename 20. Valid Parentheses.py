class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(','}':'{', ']':'[' }       
        for i in s:
            v = dic.get(i,None)
            
            if v==None:
                stack.append(i)
            else:
                if len(stack) == 0 or stack[-1]!=v:
                    return False
                else:
                    stack.pop()
        
        if len(stack)==0:
            return True
        else:
            return False
                