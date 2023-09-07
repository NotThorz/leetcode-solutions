#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#


# @lc code=start
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode = []
        max_freq = 0
        last = None  # Initialize last to None
        curr_freq = 0

        def dfs(node):
            nonlocal mode, max_freq, last, curr_freq

            if not node:
                return

            dfs(node.left)

            if last is None:
                curr_freq = 1
            elif last == node.val:
                curr_freq += 1
            else:
                curr_freq = 1

            if curr_freq > max_freq:
                max_freq, mode = curr_freq, [node.val]
            elif curr_freq == max_freq:
                mode.append(node.val)

            last = node.val

            dfs(node.right)

        dfs(root)

        return mode


# @lc code=end
