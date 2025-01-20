class Daily_Solution_7:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        Map = {}  
        row_countdowns = [m] * n
        col_countdowns = [n] * m

        for i in range(n):
            for j in range(m):
                Map[mat[i][j]] = (i, j)

        for i,num in enumerate(arr):
            row, col = Map[num]
            row_countdowns[row] -= 1
            col_countdowns[col] -= 1
            if row_countdowns[row] == 0 or col_countdowns[col] == 0:
                return i

        return 99

        
