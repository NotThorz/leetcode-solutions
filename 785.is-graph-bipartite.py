#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#


# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n  # Initialize colors, -1 represents uncolored
        queue = deque()

        for start in range(n):
            if colors[start] == -1:
                queue.append(start)
                colors[start] = 0  # Assign the first color

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if colors[neighbor] == -1:
                            colors[neighbor] = (
                                1 - colors[node]
                            )  # Assign the opposite color
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[node]:
                            return False  # Conflict, not bipartite

        return True


# @lc code=end
