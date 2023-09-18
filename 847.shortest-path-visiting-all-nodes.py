#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#

# @lc code=start
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_mask = (1 << n) - 1
        queue = deque()
        visited = set()

        for i in range(n):
            queue.append((i, 1 << i, 0))

        while queue:
            node, state, steps = queue.popleft()

            if state == target_mask:
                return steps

            for neighbor in graph[node]:
                new_state = state | (1 << neighbor)


                if (neighbor, new_state) not in visited:
                    queue.append((neighbor, new_state, steps + 1))
                    visited.add((neighbor, new_state))

        return -1  

        
# @lc code=end

