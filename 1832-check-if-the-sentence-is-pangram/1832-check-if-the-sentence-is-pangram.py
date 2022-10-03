class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        contains = [0 for i in range(26)]
        answer = True
        
        for char in sentence:
            contains[ord(char) - ord('a')] += 1
        
        for i in contains:
            if i == 0:
                answer = False
                break
            
        return answer
        