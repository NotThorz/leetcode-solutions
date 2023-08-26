#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        ans = []

        for s in stack:
            if s == "..":
                if ans:
                    ans.pop()
            elif s and s != ".":
                ans.append(s)

        return "/" + "/".join(ans)
        # @lc code=end

