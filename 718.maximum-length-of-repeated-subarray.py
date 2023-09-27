#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        s = ''.join([chr(x) for x in nums2])
        window = ''
        ans = 0
        for num in nums1:
            window+=chr(num)
            if window in s:
                ans = max(ans,len(window))
            else:
                window = window[1:]
        
        return ans
# @lc code=end

