class Solution:
    def intToRoman(self, num: int) -> str:
        
        num_list= []
        
        while(num):
            num_list.append(num%10)
            num = int(num/10)
        
        l = len(num_list)
        ans = ''
        
        key_list = [1000,500,100,50,10,5,1]
        alphabet_list = ['M','D','C','L','X','V','I']
        
        
        for c,numb in enumerate(num_list):
            new_num = 10**c * numb
            
            
            for ind,k in enumerate(key_list):
                
                r = int(new_num/k)
                
                if r!=0:
                    if numb == 4 or numb == 9:
                        ans = alphabet_list[-(2*c+1)]+alphabet_list[ind-1]+ans
                        break
                    elif numb == 6 or numb == 7 or numb == 8:
                        ans = alphabet_list[ind]+(numb-5)*alphabet_list[-(2*c+1)]+ans
                        break
                    else:
                        ans = r*alphabet_list[ind] + ans
                        break
                    
                
                
        return ans