#
# @lc app=leetcode id=2050 lang=python3
#
# [2050] Parallel Courses III
#

# @lc code=start
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n
        graph = defaultdict(list)
        
        for pre, course in relations:
            indegree[course - 1] += 1
            graph[pre - 1].append(course - 1)
        
        ans = 0
        heap =  [(time[i],i) for i in range(n) if indegree[i] == 0]
        heapify(heap)
        while heap:
            t,node = heappop(heap)
            ans=t
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(heap,(time[neighbor] + ans, neighbor))
        
        return ans
        
# @lc code=end

