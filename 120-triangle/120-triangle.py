class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = [[10e7 for y in x] for x in triangle]
        
        row_len = len(triangle)
        
        for i in range(row_len):
            col_len = len(triangle[i])
            for j in range(col_len):
                if i - 1 < 0:
                    memo[i][j] = triangle[i][j]
                elif j - 1 < 0:
                    memo[i][j] = min(memo[i][j], memo[i-1][j]) + triangle[i][j]
                elif j >= col_len - 1:
                    memo[i][j] = min(memo[i][j], memo[i-1][j-1]) + triangle[i][j]
                else:
                    memo[i][j] = min(memo[i][j], memo[i-1][j], memo[i-1][j-1]) + triangle[i][j]
        
        return min(memo[row_len-1])
                    
        