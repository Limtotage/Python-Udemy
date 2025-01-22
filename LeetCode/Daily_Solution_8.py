class Daily_Solution_8:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n=len(isWater)
        m=len(isWater[0])
        height = [[-1]*m for _ in range(n)]
        directions={(0,-1),(0,1),(1,0),(-1,0)}
        locations = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    height[i][j]=0
                    locations.append((i,j))
        while locations:
            x,y = locations.popleft()
            for dx,dy in directions:
                newx=x+dx
                newy=y+dy
                if newx>=0 and newx<n and newy>=0 and newy<m and height[newx][newy]==-1:
                    height[newx][newy] = height[x][y] + 1
                    locations.append((newx,newy))
        return height       
class Daily_Solution_8_adv:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        height = [[float('inf')] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                else:
                    if i > 0:
                        height[i][j] = min(height[i][j], height[i - 1][j] + 1)
                    if j > 0:
                        height[i][j] = min(height[i][j], height[i][j - 1] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i < n - 1:
                    height[i][j] = min(height[i][j], height[i + 1][j] + 1)
                if j < m - 1:
                    height[i][j] = min(height[i][j], height[i][j + 1] + 1)

        return height       
