class Solution:
    def isHappy(self, n: int) -> bool:
        ans = True
        nums = []
        while n != 1:
            s = str(n)
            summ = 0
            for c in s:
                summ += int(c) ** 2
            if summ in nums:
                ans = False
                break
            else:
                n = summ
                nums.append(summ)
        return ans