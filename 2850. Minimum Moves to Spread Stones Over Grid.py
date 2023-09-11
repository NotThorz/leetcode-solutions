class Solution:
    def minimumMoves(self, mat):
        empty_cells = []
        multi_stone_cells = []

        for i in range(3):
            for j in range(3):
                if mat[i][j] > 1:
                    for _ in range(mat[i][j]-1):
                        multi_stone_cells.append([i, j])
                elif mat[i][j] == 0:
                    empty_cells.append([i, j])

        total_moves = float('inf')  
        l=list(permutations(multi_stone_cells))
        for i in l:
            ans=0
            j=0
            for x,y in empty_cells:
                ans+=abs(x-i[j][0])+abs(y-i[j][1])
                j+=1
            total_moves=min(total_moves,ans)

        
        return total_moves