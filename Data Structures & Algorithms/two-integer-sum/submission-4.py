class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(0, len(nums)):
            print(nums[i])
            if (target - nums[i]) in nums:
                if target - nums[i] in ans.keys():
                    return sorted([i, ans[target - nums[i]]])
                
                
            ans[nums[i]] = i
        
        return


            
            

        