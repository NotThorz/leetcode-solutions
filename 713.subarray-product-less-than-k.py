#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        ans=0
        window=1
        start=0
        for end , num in enumerate(nums):
            window*=num
            while window>=k:
                window/=nums[start]
                start+=1
            ans+=end-start+1
        return ans
        
# @lc code=end

