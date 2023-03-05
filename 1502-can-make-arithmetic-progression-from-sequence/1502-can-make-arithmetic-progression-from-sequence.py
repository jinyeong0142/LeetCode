class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        length = len(arr)
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        ans = True
        
        for i in range(length - 1):
            if arr[i+1] - arr[i] != diff:
                ans = False
                break

        return ans