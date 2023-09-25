class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=Counter(s)
        d=Counter(t)

        for char in t :
            if char not in  s:
                return char
            else:
                if d[char]!=s[char]:
                    return char 