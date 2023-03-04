class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = 0
        nums = sorted(nums, reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                ans = nums[i] + nums[i+1] + nums[i+2]
                break
            else:
                continue
        return ans