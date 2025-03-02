class Daily_Solution_29:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i,j=0,0
        result = []
        while i<len(nums1) and j<len(nums2):
            key1,val1=nums1[i]
            key2,val2=nums2[j]
            if key1<key2:
                result.append([key1,val1])
                i+=1
            elif key2<key1:
                result.append([key2,val2])
                j+=1
            else:
                result.append([key2,val2+val1])
                j+=1 
                i+=1
        while i<len(nums1):
            result.append(nums1[i])
            i += 1
        while j<len(nums2):
            result.append(nums2[j])
            j += 1
        return result
