#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=r=res=0
        total=0
        nums.sort()

        while r<len(nums):
            total+=nums[r]
#so basically we are removing the element let s say all other elements are 0 and then we would need r-l+1)*nums[r] to make that whole window equal to nums right 
            while (r-l+1)*nums[r]>total+k:
                total-=nums[l]
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res 
# @lc code=end

