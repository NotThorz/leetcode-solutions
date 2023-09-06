#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        def list_len(node):
            curr = node
            ans = 0
            while curr:
                ans += 1
                curr = curr.next
            return ans

        n = list_len(head)

        size, remainder = divmod(n, k)

        ans = []
        curr = head

        for i in range(k):
            part_head = curr
            part_size = size + 1 if i < remainder else size

            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node

            ans.append(part_head)

        return ans


# @lc code=end
