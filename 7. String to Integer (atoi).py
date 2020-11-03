class Solution:
    def myAtoi(self, str: str) -> int:
        
        s = str.split()
        
        if len(s) == 0:
            return 0
        
        
        w = s[0]

        MAX = 2**31 - 1
        MIN = -2**31
        num = ''
        
        if w[0] == '+':
            w = w[1:]
        elif w[0] == '-':
            w = w[1:]
            num = num + '-'

        
        for c in w:
            
            if (ord(c) >= 48 and ord(c) <58):
                num = num + c
            else:
                break
        
        try:
            num = int(num)
        except:
            return 0
        
        if (num <= MIN):
            return MIN
        elif (num>= MAX):
            return MAX
        else:
            return num