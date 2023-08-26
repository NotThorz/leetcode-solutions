#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #Pure Topological sort 
        adj_list={i:[] for i in range(len(graph))}
        indegree=[0]*len(graph)
        for i , edges in enumerate(graph):
            for edge in edges:
                adj_list[edge].append(i)
                indegree[i]+=1
        q=deque([ i for i in range(len(indegree)) if indegree[i]==0])
        ans =list(q)
        while(q):
            x=q.popleft()
            for node in adj_list[x]:
                indegree[node]-=1 
                if indegree[node]==0:
                    q.append(node)
                    ans.append(node)
        ans.sort() #answer to be sorted 
        return ans
# @lc code=end

