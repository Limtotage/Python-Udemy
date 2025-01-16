class Daily_Solution_6(object):
    def xorAllNums(self, nums1, nums2):
        count1, count2 , xor1,xor2= len(nums1),len(nums2),0,0
        if count1%2!=0:
            for num in nums2:
                xor1^=num
        if count2%2!=0:
            for num in nums1:
                xor2^=num
        return xor1^xor2
        
