#
# @lc app=leetcode id=2662 lang=python3
#
# [2662] Minimum Cost of a Path With Special Roads
#


# @lc code=start
class Solution:
    def minimumCost(
        self, start: List[int], target: List[int], specialRoads: List[List[int]]
    ) -> int:
        # Pure Dijkstra
        special_road_map = defaultdict(list, {tuple(target): [(0, 0, 0)]})
        for x1, y1, x2, y2, cost in specialRoads:
            special_road_map[(x1, y1)].append((x2, y2, cost))

        distances = defaultdict(lambda: float("inf"))
        distances[tuple(start)] = 0

        priority_queue = [(0, *start)]

        while priority_queue:
            distance, x, y = heappop(priority_queue)

            if [x, y] == target:
                return distance

            for xx, yy, cost in special_road_map[(x, y)]:
                if distance + cost < distances[xx, yy]:
                    distances[xx, yy] = distance + cost
                    heappush(priority_queue, (distance + cost, xx, yy))

            for x1, y1 in special_road_map:
                new_distance = distance + abs(x1 - x) + abs(y1 - y)
                if new_distance < distances[x1, y1]:
                    distances[x1, y1] = new_distance
                    heappush(priority_queue, (new_distance, x1, y1))


# @lc code=end
