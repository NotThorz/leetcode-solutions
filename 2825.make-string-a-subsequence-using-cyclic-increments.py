#
# @lc app=leetcode id=2825 lang=python3
#
# [2825] Make String a Subsequence Using Cyclic Increments
#

# @lc code=start
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        alp={"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"}
        index=0
        for char in str1:
            if char==str2[index] or alp[char]==str2[index]:
                index+=1
            if index==len(str2):
                return True
        return False
# @lc code=end

