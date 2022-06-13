class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            
            if mid ** 2 == x:
                answer = mid
                break
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
        
        if answer == -1:
            answer = int(right)
        
        return answer
                
        