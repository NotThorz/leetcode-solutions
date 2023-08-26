#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        count = 1
        end = 0
        start = 0
        while end < len(chars) - 1:
            while end < len(chars) - 1:
                if chars[end] == chars[end + 1]:
                    end += 1
                    count += 1
                else:
                    break
            if count > 1:
                new_array = [chars[start]] + list(str(count)) #still O(1) space since max count is 2000 so it s a constant 
                chars[start:end + 1] = new_array  
                end = start + len(new_array)
                start = end
                count = 1
            else:
                start+=1
                end += 1
        
        return len(chars)



# @lc code=end

