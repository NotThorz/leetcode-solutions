#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Dijkstra's algorithm to find shortest times
        
        shortest_times = [float('inf')] * n
        shortest_times[0] = 0
        num_ways = [0] * n
        num_ways[0] = 1  # There's one way to start at intersection 0

        min_heap = [(0, 0)]  # (time, intersection)

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if time > shortest_times[node]:
                continue

            for neighbor, edge_time in graph[node]:
                if shortest_times[neighbor] > time + edge_time:
                    shortest_times[neighbor] = time + edge_time
                    num_ways[neighbor] = num_ways[node]
                    heapq.heappush(min_heap, (shortest_times[neighbor], neighbor))
                elif shortest_times[neighbor] == time + edge_time:
                    num_ways[neighbor] = (num_ways[neighbor] + num_ways[node]) % MOD

        return num_ways[n - 1]
        
# @lc code=end

