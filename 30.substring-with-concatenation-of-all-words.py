#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        if not s or not words:
            return result
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        words_count = len(words)
        if len(s)<total_len:
            return []
        
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1
        
        for i in range(word_len):
            left = right = i
            count = 0
            current_freq = defaultdict(int)
            
            while right + word_len <= len(s):
                current_word = s[right:right + word_len]
                right += word_len
                
                if current_word not in word_freq:
                    count = 0
                    left = right
                    current_freq.clear()
                else:
                    current_freq[current_word] += 1
                    count += 1
                    while current_freq[current_word] > word_freq[current_word]:
                        temp_word = s[left:left + word_len]
                        current_freq[temp_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == words_count:
                        result.append(left)
        
        return result
# @lc code=end

