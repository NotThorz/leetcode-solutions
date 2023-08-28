#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        options= ['A', 'C', 'G', 'T']
        q=deque([(startGene,0)])
        visited=set()
        visited.add(startGene)
        while q:
            for _ in range(len(q)):
                node,count=q.popleft()
                if node==endGene:
                    return count
                for j in range(8):
                    for option in options :
                        new_node=node[:j]+option +node[j+1:]
                        if new_node in bankSet and new_node not in visited:
                            visited.add(new_node)
                            q.append((new_node,count+1))
        return -1
# @lc code=end

