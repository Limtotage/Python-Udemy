class Daily_Solution_20:
    def punishmentNumber(self, n: int) -> int:
        def partition(num,target):
            if num < target or target < 0:
                return False
            if num == target:
                return True
            for m in (10,100,1000):
                if partition(num//m,target-(num%m)):
                    return True
            
        return sum(num for i in range(1,n+1) if partition(num:=i*i,i))
        
