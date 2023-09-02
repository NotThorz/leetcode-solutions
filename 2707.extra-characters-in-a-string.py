#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#


# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        @cache
        def dp(start):
            if start == n:
                return 0

            ans = dp(start + 1) + 1
            node = trie.root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.isWord:
                    ans = min(ans, dp(end + 1))
            return ans

        return dp(0)


# @lc code=end
