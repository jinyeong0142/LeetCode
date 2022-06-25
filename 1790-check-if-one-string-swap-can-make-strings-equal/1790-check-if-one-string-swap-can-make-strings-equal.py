class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        length = len(s1)
        
        count = 0
        idx = []
        
        for i in range(length):
            if s1[i] != s2[i]:
                count += 1
                idx.append(i)
            
        answer = False
        
        if count == 0:
            answer = True
        elif count == 2:
            if s1[idx[0]] == s2[idx[1]] and s1[idx[1]] == s2[idx[0]]:
                answer = True
        else:
            answer = False
        
        return answer