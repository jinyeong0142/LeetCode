class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        left_sum = [sum(nums[:i]) for i in range(length)]
        total_sum = sum(nums)
        
        answer = -1
        for i in range(0,length):
            if left_sum[i] == total_sum - nums[i] - left_sum[i]:
                answer = i
                break        
        return answer