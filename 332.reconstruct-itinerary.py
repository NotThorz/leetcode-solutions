#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#


# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adj = defaultdict(list)

        for src, dst in tickets:
            adj[src].append(dst)
        q = ["JFK"]
        res = deque()

        while q:
            node = q[-1]  # we didn t pop it

            if len(adj[node]) > 0:
                q.append(adj[node].pop())
            else:
                res.appendleft(q.pop())
        return res


# @lc code=end
