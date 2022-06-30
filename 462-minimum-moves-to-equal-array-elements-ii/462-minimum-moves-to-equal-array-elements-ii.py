class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        
        length = len(nums)
        median = nums[length//2]
        
        answer = 0
        
        for i in nums:
            answer += abs(i - median)
        
        return answer