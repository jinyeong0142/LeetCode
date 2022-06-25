class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        length = len(nums)
        answer = True
        count = 0
        
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                if count > 0:
                    answer = False
                    break
                else:
                    count += 1
                    if i == 0:
                        continue
                    elif nums[i-1] > nums[i+1]:
                        nums[i+1] = nums[i]
                    else:
                        continue
        
        return answer