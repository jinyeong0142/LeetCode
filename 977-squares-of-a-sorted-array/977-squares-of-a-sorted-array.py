class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for idx, val in enumerate(nums):
            nums[idx] = val ** 2
        nums = sorted(nums)
        return nums
        