#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def helper(arr):
            if len(arr)==1:
                return True
            for i in range(1,len(arr)):
                if arr[i-1]>arr[i]:
                    return False
            return True
            
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                tmp=nums[i]
                tmp2=nums[i-1]
                nums[i-1]=tmp
                h=helper(nums)
                nums[i-1]=tmp2
                nums[i]=tmp2
                h2=helper(nums)
                return h or h2
        return True

# @lc code=end

