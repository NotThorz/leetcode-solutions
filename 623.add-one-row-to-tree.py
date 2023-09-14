#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        level = 1
        queue = deque([root])

        while queue:
            if level == depth - 1:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    new_left = TreeNode(val)
                    new_left.left = node.left
                    node.left = new_left

                    new_right = TreeNode(val)
                    new_right.right = node.right
                    node.right = new_right

                return root

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return root


# @lc code=end
