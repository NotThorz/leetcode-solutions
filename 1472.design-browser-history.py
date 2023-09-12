#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#


# @lc code=start
class ListNode:
    def __init__(self, value="", next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        nxt = ListNode(url, None, self.curr)
        self.curr.next = nxt
        self.curr = nxt

    def back(self, steps: int) -> str:
        while self.curr.previous and steps > 0:
            self.curr = self.curr.previous
            steps -= 1
        return self.curr.value

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end
