class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        ans = 0

        for num in nums:
            prod *= num
        
        if prod > 0:
            ans = 1
        elif prod < 0:
            ans = -1
        else:
            ans = 0
        
        return ans