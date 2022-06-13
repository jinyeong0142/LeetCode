class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        cur = 0
        length = len(arr)
        while cur < length:
            if arr[cur] == 0 and cur + 1 != length and 0 < sum(arr[cur+1:length]):
                arr.insert(cur,0)
                cur = cur + 1
            cur = cur + 1
        del arr[length:]