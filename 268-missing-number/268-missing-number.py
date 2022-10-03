class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        answer = len(nums)
        
        for idx, val in enumerate(nums):
            if idx != val:
                answer = idx
                break
                
        return answer
        