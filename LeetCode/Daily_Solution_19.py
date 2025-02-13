class Daily_Solution_19:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res=0
        for i in range(len(nums)):
            min1=heapq.heappop(nums)
            if  min1<k:
                min2 = heapq.heappop(nums)
                res+=1
                heapq.heappush(nums,min1*2+min2)
        return res
            
