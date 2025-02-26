class Daily_Solution_28:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        tot_sum=max_sum=min_sum=0
        for x in nums:
            tot_sum+=x
            if max_sum<tot_sum:
                max_sum=tot_sum
            if min_sum>tot_sum:
                min_sum=tot_sum
        return max_sum-min_sum
