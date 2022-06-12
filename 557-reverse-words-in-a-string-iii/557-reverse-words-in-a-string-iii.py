class Solution:
    def reverseWords(self, s: str) -> str:
        tokens = s.split(' ')
        
        answer = ""
        for idx, token in enumerate(tokens):
            if idx == 0:
                answer = ''.join(reversed(token))
            else:
                answer = answer + ' ' + ''.join(reversed(token))
            
        return answer