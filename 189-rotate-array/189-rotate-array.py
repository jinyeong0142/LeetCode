class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        idx = k % length
        
        temp = nums[length-idx:]
        temp.extend(nums[:length-idx])
        
        for idx, val in enumerate(temp):
            nums[idx] = val