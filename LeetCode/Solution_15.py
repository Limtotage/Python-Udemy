class Solution_15:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good_count = 0
        for i in range(len(nums)):
            key = nums[i] -i
            current_count=freq.get(key,0)#   GetOrDefault
            good_count+= current_count
            freq[key]=current_count+1
        n = len(nums)
        return (n*(n-1))//2 - good_count
        
