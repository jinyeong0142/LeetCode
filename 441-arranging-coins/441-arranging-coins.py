class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        answer = 0
        
        for i in range(n+1):
            cur = (i * (i+1)) // 2
            nxt = ((i+1) * (i+2)) // 2
            
            if cur <= n and n < nxt:
                answer = i
                break
        
        return answer