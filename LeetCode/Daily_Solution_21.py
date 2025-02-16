class Daily_Solution_21:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (2 * n - 1)
        used = [False] * (n+1)
        self.backtracking(result,used,n,0)
        return result
    def backtracking(self,result,used,n,idx) -> bool:
        while idx<len(result) and result[idx]!=0:
            idx+=1
        if idx == len(result):
            return True
        for i in range(n,0,-1):
            if used[i]:
                continue
            if i==1:
                result[idx]=1
                used[1]=True
                if self.backtracking(result,used,n,idx+1):
                    return True
                result[idx]=0
                used[1]=False
            elif i+idx<len(result) and result[idx+i]==0:
                result[idx]=i
                result[idx+i]=i
                used[i]=True
                if self.backtracking(result,used,n,idx+1):
                    return True
                result[idx]=0
                result[idx+i]=0
                used[i]=False
        return False
            
