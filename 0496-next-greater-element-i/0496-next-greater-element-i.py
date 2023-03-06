class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = [-1 for i in range(10000)]

        for i, num in enumerate(nums2):
            idx[num] = i

        ans = []

        for i in nums1:
            flag = False
            for j in nums2[idx[i]:]:
                if j > i:
                    ans.append(j)
                    flag = True
                    break
            if flag == False:
                ans.append(-1)
        
        return ans
