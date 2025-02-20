class Solution_24:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res=""
        for i in range(len(nums)):
            res+= "0" if nums[i][i]!="0" else "1"
        return res
