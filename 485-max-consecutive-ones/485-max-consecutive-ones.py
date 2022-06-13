class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = ''
        for i in nums:
            temp = temp + str(i)
            
        tokens = temp.split('0')
        
        count = -1
        for token in tokens:
            count = max(count, len(token))
            
        return count