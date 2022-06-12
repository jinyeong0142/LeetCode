class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        answer = []
        flag = False
        
        for i in range(length):
            for j in range(i+1,length):
                if nums[i] + nums[j] == target:
                    answer = [i, j]
                    flag = True
                    break
            if flag == True:
                break
                
        return answer