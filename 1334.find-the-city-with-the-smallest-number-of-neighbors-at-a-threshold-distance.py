#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#


# @lc code=start
class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adj_list = defaultdict(list)
        for u, v, d in edges:
            adj_list[u].append((v, d))
            adj_list[v].append((u, d))

        def dijkstras(src):
            dist = [float("inf")] * n
            dist[src] = 0
            heap = [(0, src)]
            while heap:
                curr_cost, curr_node = heappop(heap)

                if curr_cost > distanceThreshold:
                    break

                for v, d in adj_list[curr_node]:
                    if dist[v] > dist[curr_node] + d:
                        dist[v] = dist[curr_node] + d
                        heappush(heap, (dist[v], v))
            return dist

        def get_neighbours(dist, src):
            ans = 0
            for i, d in enumerate(dist):
                if d <= distanceThreshold and i != src:
                    ans += 1
            return ans

        idx, min_len = -1, float("inf")
        for i in range(n):
            dist = dijkstras(i)
            neighbours = get_neighbours(dist, i)
            if neighbours <= min_len:
                min_len = neighbours
                idx = i
        return idx


# @lc code=end
