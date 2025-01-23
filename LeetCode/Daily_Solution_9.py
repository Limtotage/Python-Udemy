class Daily_Solution_9:
    def countServers(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        connected_row=[0]*n      
        connected_col=[0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    connected_row[i]+=1
                    connected_col[j]+=1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (connected_row[i]>1 or connected_col[j]>1):
                    ans+=1
        return ans;  
