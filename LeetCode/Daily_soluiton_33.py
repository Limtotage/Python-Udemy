class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i]%2 and arr[i+1]%2 and arr[i+2]%2:
                return True
        return False 

""" Sliding Window
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        window=[]
        if len(arr)<3:
            return False
        windowValue=1
        for i in range(3):
            windowValue*=arr[i]
            window.append(arr[i])
        if windowValue%2==1:
            return True
        for x in range(3,len(arr)):
            windowValue/=window[0]
            window.pop(0)
            window.append(arr[x])
            windowValue*=arr[x]
            if windowValue%2==1:
                return True
        return False"""

