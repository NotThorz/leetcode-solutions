#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        ans = ""
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                ans += str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                ans += "null"
            ans += " "  #to separate so in deserialize I can split
            
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        values = data.split()
        root = TreeNode(int(values[0]))
        q = deque([root])
        index = 1
        while q and index < len(values):
            node = q.popleft()
            if values[index] != "null":
                node.left = TreeNode(int(values[index]))
                q.append(node.left)
            index += 1
            if index < len(values) and values[index] != "null":
                node.right = TreeNode(int(values[index]))
                q.append(node.right)
            index += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

