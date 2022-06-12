class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        max_value = max(nums)
        max_index = nums.index(max_value)
        
        total_sum = 0
        for i in range(length):
            if i == max_index:
                continue
            if max_value < 2* nums[i]:
                max_index = -1
                break
        
        return max_index