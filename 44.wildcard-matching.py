#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#


# @lc code=start
class Solution:
    def f(self, s: str, p: str) -> bool:
        if (s, p) in self.dp:
            return self.dp[(s, p)]
        if s == p:
            self.dp[(s, p)] = True
        elif p == "*":
            self.dp[(s, p)] = True
        elif (s == "" and p != "") or (s != "" and p == ""):
            self.dp[(s, p)] = False
        elif s[0] == p[0] or p[0] == "?":
            self.dp[(s, p)] = self.f(s[1:], p[1:])
        elif p[0] == "*":
            self.dp[(s, p)] = self.f(s[1:], p) or self.f(s, p[1:])
        else:
            self.dp[(s, p)] = False
        return self.dp[(s, p)]

    def isMatch(self, s: str, p: str) -> bool:
        self.dp = {}
        n = len(s)
        m = len(p)
        a = ""
        if m != 0:
            a += p[0]
        for i in range(1, m):
            if p[i] == "*" and p[i - 1] == "*":
                continue
            else:
                a += p[i]
        return self.f(s, a)


# @lc code=end
