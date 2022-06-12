class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        number = 0
        for i in range(length-1, -1, -1):
            number += 10 ** (length - 1 - i) * digits[i]
            
        return list(str(number + 1))
        