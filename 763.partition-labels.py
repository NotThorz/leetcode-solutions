#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx={char:idx for idx,char in enumerate(s)}
        start=end=0
        res=[]
        for idx ,char in enumerate(s):
            end=max(end,last_idx[char])

            if end==idx:
                res.append(end-start+1)
                start=end+1
        return res
# @lc code=end

