class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=Counter(s)
        t=Counter(t)

        for char,v in t.items() :
            if v!=s[char]:
                return char 