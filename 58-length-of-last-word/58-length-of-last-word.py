class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = len(s.split()[-1])
        return answer