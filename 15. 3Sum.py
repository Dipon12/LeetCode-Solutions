class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        l = len(nums)
        my_val = 10**6
        
        for i in range(l):
            
            if my_val == nums[i]:
                continue
            
            
            my_val = nums[i]
            low = i+1
            high = l-1
            
            while(low<high):
                
                target = nums[low]+nums[high] + my_val
                low_val = nums[low]
                high_val = nums[high]
                
                if target == 0:
                    ans.append([my_val,nums[low],nums[high]])
                    
                               
                               
                    
                    while (low<high and low_val==nums[low]):
                        low+=1
                    while (high>low and high_val==nums[high]):
                        high-=1
                    
                               
                elif target < 1:
                    low = low+1
                else:
                    high = high - 1

   
        return ans