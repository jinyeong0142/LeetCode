class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        if target <= nums[left]:
            return 0
        
        answer = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                answer = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        if answer == -1:
            answer = right + 1
        
        return answer