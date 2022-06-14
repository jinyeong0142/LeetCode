class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_len = len(numbers)
        
        left = 0
        right = num_len - 1
        
        answer = None
        
        while left < right:
            cur = numbers[left] + numbers[right]
            
            if cur == target:
                answer = [left + 1, right + 1]
                break
            elif cur < target:
                left = left + 1
            else:
                right = right - 1
                
        return answer