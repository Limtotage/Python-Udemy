class Solution_2(object):
    def increasingTriplet(self, nums):
        Ilk=float("inf")
        Ikinci=float("inf")
        answer = [1]*len(nums)
        i=0
        while(i<len(nums)):
            if(nums[i]<=Ilk):
                Ilk=nums[i]
            elif(nums[i]<=Ikinci):
                Ikinci=nums[i]
            else:
                return True
            i+=1
        return False
