#
# @lc app=leetcode id=2653 lang=python3
#
# [2653] Sliding Subarray Beauty
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        window=SortedList([])
        start=0
        ans=[]
        for end in range(len(nums)):
            window.add(nums[end])

            if end-start+1==k:
                if window[x-1]<0:
                    ans.append(window[x-1])
                else:
                    ans.append(0)
                window.discard(nums[start])
                start+=1
        return ans 
# @lc code=end

