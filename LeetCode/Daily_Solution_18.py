class Daily_Solution_18:
    def Digit_Sum(self,num:int) ->int:
        digit_sum=0
        while num>0:
            digit_sum+=num%10
            num//=10
        return digit_sum
    def maximumSum(self, nums: List[int]) -> int:
        
        digit_sum_list = []
        for num in nums:
            curr_sum=self.Digit_Sum(num)
            digit_sum_list.append((curr_sum,num))
        digit_sum_list.sort()
        res=-1
        for index in range(1,len(digit_sum_list)):
            currindex = digit_sum_list[index][0]
            previndex = digit_sum_list[index-1][0]
            if previndex==currindex:
                temp_sum=digit_sum_list[index][1]+digit_sum_list[index-1][1]
                res = max(res,temp_sum)
        return res
        
