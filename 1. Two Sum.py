class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = len(nums)
        my_dic = {}
        
        for i in range(l):
            t = target - nums[i]
            v=my_dic.get(t,-1)
            
            if v!=-1:
                if my_dic[t]!=i:
                    return [my_dic[t],i]
            else:
                my_dic[nums[i]] = i

        
        return []
        