#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        ans = []
        cnt = defaultdict(int)
        triplet_to_id = {}

        def traverse(node):
            if not node:
                return 0
            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1

            id = triplet_to_id[triplet]
            cnt[id] += 1
            if cnt[id] == 2:
                ans.append(node)
            return id

        traverse(root)
        return ans


# @lc code=end
