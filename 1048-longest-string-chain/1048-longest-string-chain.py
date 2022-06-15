class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        length = len(words)
        memo = [1 for x in range(len(words))]
        
        words.sort(key=lambda x : len(x))
        
        for i in range(1,length):
            for j in range(i):
                if len(words[i]) - len(words[j]) != 1:
                    continue
                
                word_len = len(words[i])
                is_pre = False
                
                for k in range(word_len):
                    temp = words[i][:k] + words[i][k+1:]
                    
                    if temp == words[j]:
                        is_pre = True
                        break
                
                if is_pre == False:
                    continue
                else:
                    memo[i] = max(memo[i], memo[j] + 1)
                    
        return max(memo)
        