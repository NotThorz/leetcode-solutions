#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i , n in enumerate(nums):
            nums[i]=str(n)

        def compare(n1,n2):
            '''
            n1=3
            n2=30
            n1+n2=330
            n2+n1=303
            i want to return n1 is greater than n2 so -1  
            '''
            if n1+n2>n2+n1:
                return -1
            return 1
        nums.sort(key=cmp_to_key(compare))
        return str(int("".join(nums)))
# @lc code=end

