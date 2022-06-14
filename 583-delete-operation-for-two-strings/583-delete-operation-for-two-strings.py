class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        w1_len = len(word1)
        w2_len = len(word2)
        
        memo = [[0 for y in range(w2_len+1)] for x in range(w1_len+1)]
        
        for i in range(1, w1_len + 1):
            for j in range(1, w2_len + 1):
                if word1[i-1] == word2[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        
        answer = w1_len - memo[w1_len][w2_len] + w2_len - memo[w1_len][w2_len]
        return answer