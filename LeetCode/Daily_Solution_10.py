class Daily_Solution_10:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        visited= [[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j]>0:
                    res = max(res,self.BFS(i,j,grid,visited))
        return res
    def BFS(self,start_x,start_y,grid,visited)-> int:
        row = len(grid)
        col = len(grid[0])
        total=0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        que = deque()
        visited[start_x][start_y]=True
        que.append((start_x,start_y))
        while len(que)>0:
            x,y = que.popleft()
            total+= grid[x][y]
            for dx,dy in directions:
                newx= x+dx
                newy=y+dy
                if newx>=0 and newy>=0 and newx<row and newy<col and grid[newx][newy]>0 and not visited[newx][newy] :
                    visited[newx] [newy] = True
                    que.append((newx,newy))
        return total
        
