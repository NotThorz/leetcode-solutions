#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        startIndex = 0
        pMap, sMap = defaultdict(int),defaultdict(int)
        res = []
        
        for char in p:
            pMap[char] +=1
        
        for i in range(len(s)):
            sMap[s[i]] +=1

            if i >= len(p) - 1:
                if sMap == pMap:
                    res.append(startIndex)
                
                # If current character is in sMap, remove it and re-update the map.
                if s[startIndex] in sMap:
                    sMap[s[startIndex]] -= 1
                    if sMap[s[startIndex]] == 0:
                        del sMap[s[startIndex]]
                startIndex += 1
        
        return res
# @lc code=end

