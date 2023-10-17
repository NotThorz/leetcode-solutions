#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#

# @lc code=start
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph=defaultdict(list) #changing the problem to a graph problem for easier interaction 
        indegree=[0]*n
        for node in range(n):
            left=leftChild[node] #left is easier and the terminology fits a tree problem
            right=rightChild[node] #same as left 
            if left>=0: #the condition if the left ==-1 means there is no child , if we don t add this condition that means we will have a node -1 with many parents
                indegree[left]+=1
                graph[node].append(left)
            if right>=0:
                indegree[right]+=1
                graph[node].append(right)
        
        rc=[node for node in range(n) if indegree[node]==0] #root_candidates , if indegree is 0 then no ingoing edges
        if len(rc)!=1:
            return False
        root=rc[0] #the root of the tree is the only element that has no ingoing  edges 
        q=deque([root])
        seen=set() #storing the visited nodes to make sure there is no cycles in the tree
        seen.add(root)
        while q :
            node=q.popleft()
            for child in graph[node]:
                if child in seen:
                    return False
                seen.add(child)
                q.append(child)
        return len(seen)==n #if we have visited every node without having seen the same node twice then the tree is valid , and no node is sharing a child
# @lc code=end

