class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            if target - val in nums[i+1:]:
                yield i
                yield len(nums)-nums[::-1].index(target-val)-1
                return
        
        return 
