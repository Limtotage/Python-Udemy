class Daily_Solution_11:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr=nums[0]
        rslt=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curr+=nums[i]
            else:
                rslt=max(rslt,curr)
                curr=nums[i]
        return max(rslt,curr)
