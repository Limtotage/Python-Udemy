class Daily_Solution_32:
    def NumberofDigits(self,number)->bool:
        count = 0
        while number>0 :
            count=count+1
            number=number//10
        return count%2==0
    def findNumbers(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            if  self.NumberofDigits(num):
                res=res+1
        return res       
