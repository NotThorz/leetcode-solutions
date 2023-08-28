class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count_L=0
        count_R=0
        count__=0
        for i in moves:
            if i=='L':
                count_L+=1
            elif i=='R':
                count_R+=1
            else:
                count__+=1

        return count__+count_R-count_L if count_R>=count_L else count__+count_L-count_R

        