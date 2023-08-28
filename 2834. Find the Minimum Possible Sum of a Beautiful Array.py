class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        ans=0
        d=defaultdict(int)
        i=1
        while len(d)<n:
            if target-i not in d:
                d[i]=1
                ans+=i
            i+=1
        return ans 