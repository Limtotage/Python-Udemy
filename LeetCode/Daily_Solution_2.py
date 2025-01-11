class Daily_Solution_2(object):
    def canConstruct(self, s, k):
        if k>len(s): 
            return False
        chars = [0]*26
        for c in s:
            chars[ord(c)-ord('a')]+=1
        oddcounter =0
        for i in range(26):
            if(chars[i]%2==1):
                oddcounter+=1
        return oddcounter<=k 
        
